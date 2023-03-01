from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=8)
    email = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nombre} - {self.apellido_paterno}"
    

    class Meta:
        db_table = "clientes"