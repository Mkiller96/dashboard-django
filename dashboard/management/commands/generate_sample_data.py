from django.core.management.base import BaseCommand
from dashboard.models import SalesData
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Genera datos de ejemplo para el dashboard'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes
        SalesData.objects.all().delete()
        
        # Configuración
        productos = [
            ('Laptop HP', 'Electrónica'),
            ('Mouse Logitech', 'Electrónica'),
            ('Teclado Mecánico', 'Electrónica'),
            ('Monitor Samsung', 'Electrónica'),
            ('Escritorio Ergonómico', 'Muebles'),
            ('Silla Oficina', 'Muebles'),
            ('Lámpara LED', 'Iluminación'),
            ('Cámara Web', 'Electrónica'),
            ('Audífonos Bluetooth', 'Electrónica'),
            ('Tablet Android', 'Electrónica'),
            ('Smartphone Samsung', 'Electrónica'),
            ('Smartwatch', 'Electrónica'),
            ('Impresora HP', 'Electrónica'),
            ('Router WiFi', 'Electrónica'),
            ('Disco Duro 1TB', 'Electrónica'),
            ('Memoria USB 64GB', 'Electrónica'),
            ('Cable HDMI', 'Accesorios'),
            ('Adaptador USB-C', 'Accesorios'),
            ('Mousepad Gaming', 'Accesorios'),
            ('Estante Libros', 'Muebles'),
        ]
        
        regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
        
        # Generar datos de los últimos 6 meses
        fecha_inicio = datetime.now() - timedelta(days=180)
        datos_creados = 0
        
        for dia in range(180):
            fecha = fecha_inicio + timedelta(days=dia)
            
            # Generar entre 3 y 10 ventas por día
            num_ventas = random.randint(3, 10)
            
            for _ in range(num_ventas):
                producto, categoria = random.choice(productos)
                region = random.choice(regiones)
                
                # Precios según categoría
                if categoria == 'Electrónica':
                    precio = round(random.uniform(50, 1500), 2)
                elif categoria == 'Muebles':
                    precio = round(random.uniform(100, 800), 2)
                elif categoria == 'Iluminación':
                    precio = round(random.uniform(20, 150), 2)
                else:
                    precio = round(random.uniform(10, 100), 2)
                
                cantidad = random.randint(1, 5)
                
                SalesData.objects.create(
                    date=fecha.date(),
                    product=producto,
                    category=categoria,
                    quantity=cantidad,
                    price=precio,
                    region=region
                )
                datos_creados += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'✓ Se crearon {datos_creados} registros de ventas exitosamente')
        )
