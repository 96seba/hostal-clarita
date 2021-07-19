from django.urls import path
from .views import index, consulta_proveedores, detalle_op, registro_empleado, listar_empleados

urlpatterns = [
    path('', index, name='index'),
    path('proveedores/', consulta_proveedores, name='consulta_proveedores'),
    path('proveedores/pedido/<int:id_op>', detalle_op, name='detalle_op'),
    path('Usuarios/registro_empleado.html', registro_empleado, name='registro_empleado'),
    path('lista_empleado', listar_empleados, name='listar_empleados'),

]
