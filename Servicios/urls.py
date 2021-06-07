from django.urls import path
from .views import (listar_ordenes, borrar_orden, cmb_ordenes, generar_ordenPedido,)

urlpatterns = [
    path('listarOrdenes', listar_ordenes, name='listar_ordenes'),
    path('borrar_orden/<int:id_orden_pedido>', borrar_orden, name='borrar_orden'),
    path('recepcionProductos', cmb_ordenes, name='cmb_ordenes'),
    path('generarOrdenPedido', generar_ordenPedido, name='generar_ordenPedido'),
]
