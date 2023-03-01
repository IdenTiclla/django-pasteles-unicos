from django.db import models


from clientes.models import Cliente
from pasteles.models import Producto

# Create your models here.




class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    # pasteles = models.ManyToManyField(Pastel, through='DetallePedido')
    imagen = models.ImageField(null=False, blank=False)
    descripcion_tematica = models.CharField(max_length=250)

    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()

    entregado = models.BooleanField(default=False)


    class Meta:
        db_table = "pedidos"

    def __str__(self):
        return f"<{self.cliente.nombre}>"



# class DetallePedido(models.Model):
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#     pastel = models.ForeignKey(Pastel, on_delete=models.CASCADE)
#     descripcion_tematica = models.CharField(max_length=255)


#     class Meta:
#         db_table = "detalle_pedido"

# pensar mas

class Foto(models.Model):
    # pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE)
    imagen = models.ImageField(null=False, blank=False)


    class Meta:
        db_table = "Tematica"