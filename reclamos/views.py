from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from clientes.models import Cliente
from .models import Reclamo
# Create your views here.


def reclamos(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        reclamos = Reclamo.objects.all()
        return render(request, "reclamos/reclamos.html", {
            'clientes': clientes,
            'reclamos': reclamos
        })
    
    elif request.method == "POST":
        cliente_id = request.POST['cliente_id']
        cliente = Cliente.objects.get(id=cliente_id)

        descripcion = request.POST['descripcion_reclamo']
        
        reclamo = Reclamo(cliente=cliente, descripcion=descripcion)
        reclamo.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Reclamos Registrados exitosamente")
        return redirect('/reclamos')