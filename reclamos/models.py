from django.db import models

from datetime import datetime
from clientes.models import Cliente

# Create your models here.

class Reclamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now=True)

    class Meta:
        db_table = "reclamos"

    def __str__(self):
        return f"<{self.descripcion}>"