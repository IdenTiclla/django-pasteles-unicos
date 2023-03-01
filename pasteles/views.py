from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Producto

# from .models import Tamaño, Sabor


# Create your views here.

def index(request):
    return render(request, "index.html")



# def tamaños(request):
#     if request.method == "GET":
#         tamaños = Tamaño.objects.all()
#         return render(request, "tamaños/tamaños.html", {
#             'tamaños': tamaños
#         })
    
#     elif request.method == "POST":
#         nombre = request.POST['nombre']
#         tamaño = Tamaño(nombre=nombre)
#         tamaño.save()
#         messages.add_message(request=request, level=messages.SUCCESS, message="Tamaño registrado exitosamente!")
#         return redirect('/tamaños')


def productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        return render(request, "productos/productos.html", {
            'productos': productos
        })
    elif request.method == 'POST':
        print(request.POST)
        nombre = request.POST['nombre']
        tamaño = request.POST['tamaño']
        sabor = request.POST['sabor']
        precio = request.POST['precio']

        producto = Producto(nombre=nombre, tamaño=tamaño, sabor=sabor, precio=precio)
        producto.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Producto registrado exitosamente!")
        return redirect("/productos")


def actualizar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == "GET":
        return render(request, "productos/actualizar_producto.html", {
            'producto': producto
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        tamaño = request.POST['tamaño']
        sabor = request.POST['sabor']
        precio = request.POST['precio']

        producto.nombre = nombre
        producto.tamaño = tamaño
        producto.sabor = sabor
        producto.precio = precio

        producto.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Producto Actualizado exitosamente!")
        return redirect('/productos')


def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Producto Eliminado exitosamente!")

    return redirect("/productos")