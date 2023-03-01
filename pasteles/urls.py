from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('productos', views.productos),
    path("productos/update/<int:id_producto>", views.actualizar_producto),
    path("productos/delete/<int:id_producto>", views.eliminar_producto)
    
]
