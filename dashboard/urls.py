from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('sales/', views.sales_report, name='sales_report'),
    path('api/chart-data/', views.get_chart_data, name='chart_data'),
]
