#!/bin/bash
# Script para inicializar la aplicación en Render

echo "Ejecutando migraciones..."
python manage.py migrate --noinput

echo "Generando datos de ejemplo..."
python manage.py generate_sample_data

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "¡Aplicación lista!"
