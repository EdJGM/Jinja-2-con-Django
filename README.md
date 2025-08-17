# Jinga2 Lab 2 - Django Inventario de Productos

Este proyecto es una aplicación web desarrollada con Django que permite gestionar un inventario de productos. Utiliza plantillas Jinja2 para la presentación y proporciona funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para los productos.

## Características
- Listado de productos
- Crear, editar y eliminar productos
- Importar y exportar productos
- Interfaz moderna con plantillas personalizadas

## Estructura del Proyecto
- `inventario/`: Configuración principal de Django
- `productos/`: Aplicación principal para la gestión de productos
- `templates/`: Plantillas HTML (Jinja2)
- `img/`: Imágenes utilizadas en la interfaz
- `db.sqlite3`: Base de datos SQLite
- `requirements.txt`: Dependencias del proyecto

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
4. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso
Accede a la aplicación en [http://localhost:8000/](http://localhost:8000/) y utiliza las opciones del menú para gestionar el inventario de productos.

## Requisitos
- Python 3.11+
- Django
- Jinja2

## Créditos
Desarrollado por EdJGM para el curso de Desarrollo Web Avanzado.

## Licencia
Este proyecto es solo para fines educativos.
