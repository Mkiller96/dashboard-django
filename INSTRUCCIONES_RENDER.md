# ✅ CONFIGURACIÓN PARA RENDER - DASHBOARD DJANGO

## 📋 CONFIGURACIÓN DEL WEB SERVICE

### Build & Deploy Settings

**Name:** `dashboard-django`

**Root Directory:** `dashboard_django`

**Build Command:** `bash build.sh`

**Start Command:** `gunicorn dashboard_project.wsgi:application`

**Environment:** Python 3

---

## 🔑 VARIABLES DE ENTORNO

Configura estas 2 variables en "Environment":

```
SECRET_KEY=genera_una_clave_secreta_diferente_aqui
DEBUG=False
```

**Para generar SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

**Opcional:**
- `ALLOWED_HOSTS` - Si quieres especificar hosts adicionales (por defecto incluye .onrender.com)

---

## ✅ PASOS PARA DESPLEGAR

1. Sube los cambios a GitHub:
   ```bash
   cd C:\Users\MS\Documents\portafolio
   git add dashboard_django/
   git commit -m "Configurar Dashboard Django para Render"
   git push
   ```

2. En Render:
   - **New +** → **Web Service**
   - Conecta tu repositorio
   - Usa la configuración de arriba
   - Añade las variables de entorno
   - Click **"Create Web Service"**

3. Espera 5-7 minutos (Django tarda más que Flask)

4. ¡Listo! Tu dashboard estará funcionando

---

## 📊 QUÉ HACE EL BUILD AUTOMÁTICAMENTE

- ✅ Instala todas las dependencias (Django, pandas, numpy, etc.)
- ✅ Ejecuta migraciones de base de datos
- ✅ Genera datos de ejemplo para las gráficas
- ✅ Recolecta archivos estáticos con WhiteNoise
- ✅ Todo listo para producción

---

## 🎨 CARACTERÍSTICAS

El dashboard incluye:
- 📈 Gráficas de ventas mensuales
- 📊 Análisis de productos
- 💰 Reportes financieros
- 🔄 Datos de ejemplo precargados
- 📱 Diseño responsive

---

## ⚠️ NOTAS IMPORTANTES

- La base de datos es SQLite (se reinicia en cada deploy en el plan gratuito)
- Los datos de ejemplo se regeneran automáticamente
- WhiteNoise sirve los archivos estáticos automáticamente
- El servicio se "duerme" después de 15 min de inactividad (plan gratuito)
