from django.urls import path
from .views import (
    registro_cliente,
    listar_ordenes_compra,
    registro_orden_compra,
    editar_orden_compra,
    eliminar_orden_compra,
    listar_facturas,
    generar_factura,
    detalle_factura,
    anular_factura,
    registro_habitacion,
    listar_habitacion
)

urlpatterns = [
    path('registro/', registro_cliente, name='registro_cliente'),
    path('ordenes_compra/', listar_ordenes_compra, name='listar_ordenes_compra'),
    path('ordenes_compra/ingresar/', registro_orden_compra, name='registro_orden_compra'),
    path('ordenes_compra/detalle/<int:oc_id>', editar_orden_compra, name='editar_orden_compra'),
    path('ordenes_compra/eliminar/<int:oc_id>', eliminar_orden_compra, name='eliminar_orden_compra'),
    path('facturas/', listar_facturas, name='listar_facturas'),
    path('facturas/generar/<int:oc_id>', generar_factura, name='generar_factura'),
    path('facturas/detalle/<int:id_factura>', detalle_factura, name='detalle_factura'),
    path('facturas/anular/<int:id_factura>', anular_factura, name='anular_factura'),
    path('habitacion/registro/', registro_habitacion, name='registro_habitacion'),
    path('habitacion/', listar_habitacion, name='listar_habitacion')
]
