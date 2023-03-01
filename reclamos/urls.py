from django.urls import path, include

from . import views

urlpatterns = [
    path("reclamos", views.reclamos)
]