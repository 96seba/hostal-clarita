from django.urls import path
from .views import index, consulta_proveedores, detalle_op

urlpatterns = [
    path('', index, name='index'),
    path('proveedores/', consulta_proveedores, name='consulta_proveedores'),
    path('proveedores/pedido/<int:id_op>', detalle_op, name='detalle_op'),
]
