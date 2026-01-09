#!/bin/bash

# Script de configuración rápida para el Dashboard Django

echo "🚀 Configurando Dashboard de Análisis Django..."

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python -m venv venv

# Activar entorno virtual (Linux/Mac)
if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    source venv/bin/activate
fi

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar migraciones
echo "🗄️  Ejecutando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Generar datos de ejemplo
echo "📊 Generando datos de ejemplo..."
python manage.py generate_sample_data

# Crear superusuario
echo "👤 Crear superusuario (admin panel)"
python manage.py createsuperuser

echo "✅ Configuración completa!"
echo ""
echo "Para iniciar el servidor, ejecuta:"
echo "python manage.py runserver"
echo ""
echo "Luego abre tu navegador en: http://localhost:8000"
