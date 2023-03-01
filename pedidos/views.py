from datetime import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Cliente, Pedido, Producto

# nuevos imports para el pdf

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

# Create your views here.


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def realizar_pedido(request):
    if request.method == "GET":
        cliente = Cliente.objects.all()

        productos = Producto.objects.all()

        return render(request, "pedidos/realizar_pedido.html", {
            'clientes': cliente,
            'productos': productos
        })

    elif request.method == "POST":
        cliente_id = request.POST['cliente_id']
        cliente = Cliente.objects.get(id=cliente_id)
        
        # pasteles_id = request.POST['pasteles_id']
        productos_id = request.POST.getlist('productos_id')
        
        print(f"post pasteles id: {request.POST['productos_id']}")
        imagen = request.FILES.get('imagen')
        descripcion_tematica = request.POST['descripcion_tematica']
        pedido = Pedido(cliente=cliente)


        fecha_pedido = request.POST['fecha_pedido']
        fecha_entrega = request.POST['fecha_entrega']

        fecha_pedido_obj = datetime.strptime(fecha_pedido, '%m/%d/%Y')
        fecha_entrega_obj = datetime.strptime(fecha_entrega, '%m/%d/%Y')
        
        pedido.fecha_pedido = fecha_pedido_obj
        pedido.fecha_entrega = fecha_entrega_obj


        pedido.imagen = imagen
        pedido.descripcion_tematica = descripcion_tematica



        pedido.save()
        print(f"pasteles_id: {productos_id}")
        for producto_id in productos_id:
            producto = Producto.objects.get(id=producto_id)
            pedido.productos.add(producto)
            pedido.save()



        print(request.POST)

        
        
        # imagenes = request.FILES.getlist('images')
        
        # print(request.FILES)
        # print(cliente_id)
        
        # cliente = Cliente.objects.get(id=cliente_id)

        # pedido = Pedido()
        # pedido.cliente = cliente
        # pedido.save()

        # for imagen in imagenes:
        #     f = Foto.objects.create(
        #         pedido = pedido,
        #         imagen = imagen
        #     )

        #     pedido.foto_set.add(f)

        # # cliente = Cliente.objects.get(id=cliente_id)
        # # pedido = Pedido()
        # # pedido.cliente = cliente









        messages.add_message(request=request, level=messages.SUCCESS, message="Pedido Realizado exitosamente!")
        return redirect('/realizar_pedido')
    

def mis_pedidos(request):
    # pedidos = Pedido.objects.all()
    pedidos = Pedido.objects.filter(entregado=False)

    return render(request, "pedidos/mis_pedidos.html", {
        'pedidos': pedidos
    })


def obtener_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    total = 0
    for producto in pedido.productos.all():
        total += producto.precio
    
    print(total)

    return render(request, "pedidos/pedido.html", {
        'pedido': pedido,
        'total': total
    })


def entregar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.entregado = True
    pedido.save()

    messages.add_message(request=request, level=messages.SUCCESS, message="Pedido entregado exitosamente!")
    return redirect('/mis_pedidos')
    

def pedidos_entregados(request):
    # pedidos = Pedido.objects.all()
    pedidos = Pedido.objects.filter(entregado=True)

    return render(request, "pedidos/pedidos_entregados.html", {
        'pedidos': pedidos
    })


#  ruta para descargar el comprobante
def descargar_comprobante(request, id):
    pedido = Pedido.objects.get(id=id)
    cliente = pedido.cliente
    nombre_completo = f"{cliente.nombre} {cliente.apellido_paterno} {cliente.apellido_materno}"
    email = cliente.email
    telefono = cliente.telefono

    total = 0
    productos = pedido.productos.all()
    for producto in productos:
        total += producto.precio
    
    data = {
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",
	"website": "pastelesunicos.com",


	"company": nombre_completo,
	"phone": cliente.telefono,
    "productos": productos,
	"email": email,
    "total": total
	}
    pdf = render_to_pdf("pedidos/pdf_template_comprobante.html", data)
    return HttpResponse(pdf, content_type='application/pdf')