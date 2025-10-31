# Examen — Monitoreo del Sistema con Django y psutil

Información del grupo:
- Nombre(s): Josseth Bautista, Oscar Hernández
- Número(s) de cuenta: 201810020200, 200711120001

Descripción
Este proyecto implementa una aplicación Django llamada `monitor` con una app interna `sistema` que muestra en tiempo real métricas del sistema usando la librería `psutil`. La interfaz permite actualización manual (botón) y automática (JavaScript, configurada por defecto a 5s).

Contenido
- manage.py
- monitor/ (proyecto Django)
- sistema/ (app Django)
  - templates/sistema/index.html
  - static/sistema/js/update.js
- requirements.txt
- Dockerfile
- docker-compose.yml
- GROUP.txt (archivo con identificación del grupo)

Requisitos
- Linux (probado en Ubuntu/Debian)
- Docker & docker-compose OR Python 3.11+ y virtualenv

Instalación y ejecución (local, sin Docker)
1. Clonar el repositorio o descargar los archivos.
2. Crear entorno virtual:
   python3 -m venv venv
   source venv/bin/activate
3. Instalar dependencias:
   pip install -r requirements.txt
4. Migraciones y ejecución:
   python manage.py migrate
   python manage.py runserver 0.0.0.0:8000
5. Abrir en el navegador: http://localhost:8000/

Ejecución con Docker (recomendado)
1. Construir y levantar:
   docker-compose up --build
2. Abrir en el navegador: http://localhost:8000/

Notas:
- /api/metrics/ es el endpoint JSON para la actualización por AJAX.
