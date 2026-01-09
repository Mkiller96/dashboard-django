from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg, Count, Max, Min
from .models import SalesData, Metric
import pandas as pd
from datetime import datetime, timedelta
from decimal import Decimal


def index(request):
    """Vista principal del dashboard con KPIs y resumen"""
    # Calcular KPIs principales
    total_sales = SalesData.objects.aggregate(
        total_revenue=Sum('revenue'),
        total_quantity=Sum('quantity'),
        avg_price=Avg('price')
    )
    
    # Obtener datos recientes
    recent_sales = SalesData.objects.all()[:10]
    
    # Ventas por categoría
    sales_by_category = SalesData.objects.values('category').annotate(
        total=Sum('revenue'),
        count=Count('id')
    ).order_by('-total')
    
    # Ventas por región
    sales_by_region = SalesData.objects.values('region').annotate(
        total=Sum('revenue')
    ).order_by('-total')
    
    context = {
        'total_revenue': total_sales['total_revenue'] or 0,
        'total_quantity': total_sales['total_quantity'] or 0,
        'avg_price': total_sales['avg_price'] or 0,
        'recent_sales': recent_sales,
        'sales_by_category': sales_by_category,
        'sales_by_region': sales_by_region,
        'total_products': SalesData.objects.values('product').distinct().count(),
    }
    
    return render(request, 'dashboard/index.html', context)


def analytics(request):
    """Vista de análisis avanzado con pandas"""
    # Convertir QuerySet a DataFrame
    sales_data = SalesData.objects.all().values(
        'date', 'product', 'category', 'quantity', 'price', 'revenue', 'region'
    )
    
    if sales_data:
        df = pd.DataFrame(list(sales_data))
        
        # Análisis estadístico
        stats = {
            'revenue_mean': float(df['revenue'].mean()) if len(df) > 0 else 0,
            'revenue_median': float(df['revenue'].median()) if len(df) > 0 else 0,
            'revenue_std': float(df['revenue'].std()) if len(df) > 0 else 0,
            'quantity_mean': float(df['quantity'].mean()) if len(df) > 0 else 0,
            'top_product': df.groupby('product')['revenue'].sum().idxmax() if len(df) > 0 else 'N/A',
            'top_category': df.groupby('category')['revenue'].sum().idxmax() if len(df) > 0 else 'N/A',
        }
        
        # Ventas por día
        df['date'] = pd.to_datetime(df['date'])
        daily_sales = df.groupby('date')['revenue'].sum().reset_index()
        daily_sales = daily_sales.sort_values('date')
        
        # Top 10 productos
        top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(10)
        
    else:
        stats = {
            'revenue_mean': 0,
            'revenue_median': 0,
            'revenue_std': 0,
            'quantity_mean': 0,
            'top_product': 'N/A',
            'top_category': 'N/A',
        }
        daily_sales = pd.DataFrame()
        top_products = pd.Series()
    
    context = {
        'stats': stats,
        'daily_sales': daily_sales.to_dict('records') if len(daily_sales) > 0 else [],
        'top_products': top_products.to_dict() if len(top_products) > 0 else {},
    }
    
    return render(request, 'dashboard/analytics.html', context)


def sales_report(request):
    """Reporte detallado de ventas"""
    # Filtros
    category = request.GET.get('category', None)
    region = request.GET.get('region', None)
    
    sales = SalesData.objects.all()
    
    if category:
        sales = sales.filter(category=category)
    if region:
        sales = sales.filter(region=region)
    
    # Obtener todas las categorías y regiones para filtros
    categories = SalesData.objects.values_list('category', flat=True).distinct()
    regions = SalesData.objects.values_list('region', flat=True).distinct()
    
    context = {
        'sales': sales[:50],  # Limitar a 50 resultados
        'categories': categories,
        'regions': regions,
        'selected_category': category,
        'selected_region': region,
    }
    
    return render(request, 'dashboard/sales_report.html', context)


def get_chart_data(request):
    """API endpoint para datos de gráficos"""
    chart_type = request.GET.get('type', 'sales_by_month')
    
    if chart_type == 'sales_by_month':
        # Ventas por mes
        sales_data = SalesData.objects.all().values('date', 'revenue')
        df = pd.DataFrame(list(sales_data))
        
        if len(df) > 0:
            df['date'] = pd.to_datetime(df['date'])
            df['month'] = df['date'].dt.to_period('M')
            monthly = df.groupby('month')['revenue'].sum()
            
            data = {
                'labels': [str(m) for m in monthly.index],
                'values': [float(v) for v in monthly.values]
            }
        else:
            data = {'labels': [], 'values': []}
    
    elif chart_type == 'sales_by_category':
        # Ventas por categoría
        sales = SalesData.objects.values('category').annotate(
            total=Sum('revenue')
        ).order_by('-total')
        
        data = {
            'labels': [s['category'] for s in sales],
            'values': [float(s['total']) for s in sales]
        }
    
    elif chart_type == 'sales_by_region':
        # Ventas por región
        sales = SalesData.objects.values('region').annotate(
            total=Sum('revenue')
        ).order_by('-total')
        
        data = {
            'labels': [s['region'] for s in sales],
            'values': [float(s['total']) for s in sales]
        }
    
    else:
        data = {'labels': [], 'values': []}
    
    return JsonResponse(data)
