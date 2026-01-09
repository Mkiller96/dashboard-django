@echo off
REM Script de configuración rápida para Windows

echo 🚀 Configurando Dashboard de Análisis Django...

REM Crear entorno virtual
echo 📦 Creando entorno virtual...
python -m venv venv

REM Activar entorno virtual
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo 📥 Instalando dependencias...
pip install -r requirements.txt

REM Ejecutar migraciones
echo 🗄️  Ejecutando migraciones...
python manage.py makemigrations
python manage.py migrate

REM Generar datos de ejemplo
echo 📊 Generando datos de ejemplo...
python manage.py generate_sample_data

REM Crear superusuario
echo 👤 Crear superusuario (admin panel)
python manage.py createsuperuser

echo.
echo ✅ Configuración completa!
echo.
echo Para iniciar el servidor, ejecuta:
echo python manage.py runserver
echo.
echo Luego abre tu navegador en: http://localhost:8000
pause
