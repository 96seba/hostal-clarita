from django.urls import path
from .views import (listar_ordenes, borrar_orden, cmb_ordenes, generar_ordenPedido,listar_detalle_pedido, listar_servicio_comedor, registro_servicio_comedor, registro_plato)

urlpatterns = [
    path('listarOrdenes', listar_ordenes, name='listar_ordenes'),
    path('borrar_orden/<int:id_orden_pedido>', borrar_orden, name='borrar_orden'),
    path('recepcionProductos', cmb_ordenes, name='cmb_ordenes'),
    path('generarOrdenPedido', generar_ordenPedido, name='generar_ordenPedido'),
    path('detalleOrdenProducto/<int:id_orden_pedido>', listar_detalle_pedido, name='listar_detalle_pedido'),
    path('listarDetalle', listar_detalle_pedido, name="detalle_pedido"),
    path('listarComedor', listar_servicio_comedor, name="listar_servicio_comedor"),
    path('registroComedor', registro_servicio_comedor, name="registro_servicio_comedor"),
    path('registroPlatos', registro_plato, name="registro_plato"),

]
