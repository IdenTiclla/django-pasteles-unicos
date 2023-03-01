from django.urls import path, include

from . import views

urlpatterns = [
    path("clientes", views.clientes),
    path("clientes/update/<int:id_cliente>", views.actualizar_cliente),
    path("clientes/delete/<int:id_cliente>", views.eliminar_cliente)

]