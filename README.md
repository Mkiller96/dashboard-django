# Dashboard de Análisis de Datos - Django

Dashboard interactivo para visualización y análisis de datos empresariales desarrollado con Django, Pandas y Chart.js.

## Características

- 📊 Visualización interactiva de datos con gráficos dinámicos
- 📈 Análisis estadístico en tiempo real
- 💼 Gestión de datos de ventas y rendimiento
- 🎨 Interfaz moderna y responsive
- 📱 Compatible con dispositivos móviles

## Tecnologías

- **Backend**: Django 5.0
- **Análisis de datos**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualización**: Chart.js
- **Base de datos**: SQLite (development)

## Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Cargar datos de ejemplo
python manage.py loaddata initial_data.json

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

## Uso

Accede a `http://localhost:8000` para ver el dashboard.

## Funcionalidades

- Vista general con KPIs principales
- Gráficos de ventas por período
- Análisis de tendencias
- Reportes exportables
- Panel de administración completo

## Autor

Desarrollado para portafolio profesional - 2026
