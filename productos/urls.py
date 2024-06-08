from django.urls import path
from .views import listar_productos, crear_producto, editar_producto, eliminar_producto, importar_productos_csv, exportar_productos_csv

urlpatterns = [
    # URLs de vistas normales
    path('', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('productos/importar/', importar_productos_csv, name='importar_productos_csv'),
    path('productos/exportar/', exportar_productos_csv, name='exportar_productos_csv'),
]