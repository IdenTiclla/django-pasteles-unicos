from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Cliente
# Create your views here.

def clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, "clientes/clientes.html", {
            'clientes': clientes
        })
    elif request.method == "POST":
        nombre = request.POST['nombre']
        apellido_paterno = request.POST['apellidoPaterno']
        apellido_materno = request.POST['apellidoMaterno']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']

        cliente = Cliente(nombre=nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, direccion=direccion, telefono=telefono, email=email)
        cliente.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Cliente registrado exitosamente!")
        return redirect('/clientes')


def actualizar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "GET":
        return render(request, "clientes/actualizar_cliente.html", {
            'cliente': cliente
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        apellido_paterno = request.POST['apellidoPaterno']
        apellido_materno = request.POST['apellidoMaterno']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']

        cliente.nombre = nombre
        cliente.apellido_paterno = apellido_paterno
        cliente.apellido_materno = apellido_materno
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.email = email

        cliente.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Cliente Actualizado exitosamente!")
        return redirect('/clientes')


def eliminar_cliente(request, id_cliente):
    empleado = Cliente.objects.get(id=id_cliente)
    
    empleado.delete()
    
    messages.add_message(request=request, level=messages.SUCCESS, message="Cliente Eliminado exitosamente!")

    return redirect("/clientes")