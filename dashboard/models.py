from django.db import models
from django.utils import timezone


class SalesData(models.Model):
    """Modelo para almacenar datos de ventas"""
    date = models.DateField(verbose_name='Fecha')
    product = models.CharField(max_length=100, verbose_name='Producto')
    category = models.CharField(max_length=50, verbose_name='Categoría')
    quantity = models.IntegerField(verbose_name='Cantidad')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    revenue = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ingresos')
    region = models.CharField(max_length=50, verbose_name='Región')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Dato de Venta'
        verbose_name_plural = 'Datos de Ventas'
        ordering = ['-date']

    def __str__(self):
        return f"{self.product} - {self.date}"

    def save(self, *args, **kwargs):
        # Calcular ingresos automáticamente
        if not self.revenue:
            self.revenue = self.quantity * self.price
        super().save(*args, **kwargs)


class Metric(models.Model):
    """Modelo para métricas y KPIs"""
    name = models.CharField(max_length=100, verbose_name='Nombre')
    value = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor')
    unit = models.CharField(max_length=20, verbose_name='Unidad', blank=True)
    date = models.DateField(default=timezone.now, verbose_name='Fecha')
    description = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Métrica'
        verbose_name_plural = 'Métricas'
        ordering = ['-date', 'name']

    def __str__(self):
        return f"{self.name}: {self.value} {self.unit}"
