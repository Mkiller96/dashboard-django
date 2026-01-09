from django.contrib import admin
from .models import SalesData, Metric


@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'product', 'category', 'quantity', 'price', 'revenue', 'region']
    list_filter = ['category', 'region', 'date']
    search_fields = ['product', 'category']
    date_hierarchy = 'date'
    ordering = ['-date']


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'unit', 'date']
    list_filter = ['name', 'date']
    search_fields = ['name', 'description']
    date_hierarchy = 'date'
