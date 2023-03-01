from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("realizar_pedido", views.realizar_pedido),
    path("mis_pedidos", views.mis_pedidos),
    path("pedidos_entregados", views.pedidos_entregados),
    path("pedido/comprobante/<int:id>", views.descargar_comprobante),
    
    path("pedido/<int:id>", views.obtener_pedido),
    path("pedido/entregar/<int:id>", views.entregar_pedido),

    # pedido/entregar/{{pedido.id}}

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)