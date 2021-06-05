from django.urls import path
from .views import (listar_ordenes, borrar_orden)

urlpatterns = [
    path('listarOrdenes', listar_ordenes, name="listar_ordenes"),
    path('borrar_orden/<int:id_orden_pedido>', borrar_orden, name="borrar_orden"),
]
