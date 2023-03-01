from django.db import models

# Create your models here.


    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    
    sabor = models.CharField(max_length=50)
    precio = models.IntegerField()
    #disponible = models.BooleanField(default=False)

    def __str__(self):
        return f"<{self.nombre} - {self.precio}>"

    class Meta:
        db_table = "productos"

    


    

