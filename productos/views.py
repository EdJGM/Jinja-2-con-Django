from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponse
import csv
from django.core.exceptions import ValidationError
from decimal import Decimal, InvalidOperation

productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Redirige a la lista de productos después de crear uno nuevo
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})


def exportar_productos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre; Precio; Cantidad'])  # Escribir encabezados de columnas

    productos = Producto.objects.all()
    for producto in productos:
        # Utilizar comas como delimitadores de campos
        writer.writerow([producto.nombre + '; ' + str(producto.precio) + '; ' + str(producto.cantidad)])

    return response


def importar_productos_csv(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        archivo_csv = request.FILES['archivo_csv']

        if not archivo_csv.name.endswith('.csv'):
            # Manejar error si el archivo no es CSV
            pass

        # Lee el contenido del archivo como texto
        texto_csv = archivo_csv.read().decode('utf-8').splitlines()

        csv_data = csv.reader(texto_csv, delimiter=';')  # Cambiar el delimitador a punto y coma
        for index, row in enumerate(csv_data):
            try:
                nombre = row[0]
                precio = Decimal(row[1])  # Convierte el valor a Decimal
                cantidad = int(row[2])  # Convierte el valor a entero si es necesario

                _, created = Producto.objects.update_or_create(
                    nombre=nombre,
                    defaults={'precio': precio, 'cantidad': cantidad}
                )
            except (IndexError, ValueError, ValidationError, InvalidOperation) as e:  # Usa InvalidOperation
                # Manejar errores de índice, valores no válidos, etc.
                print(f"Error en la línea {index + 1}: {e}")
                # Puedes agregar aquí un manejo específico para los valores problemáticos, como saltar la línea o registrar el error en algún archivo de registro

    return redirect('listar_productos')
