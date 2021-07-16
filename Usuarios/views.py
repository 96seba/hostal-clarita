from django.shortcuts import render, redirect
from Servicios.models import Proveedor, OrdenPedido, DetalleOrdenPedido
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    if request.user.is_authenticated:
        return redirect('panel')
    return render(request, 'Usuarios/index.html')


def consulta_proveedores(request):
    if request.method == 'POST':
        rut = request.POST.get('rut_proveedor')
        try:
            proveedor = Proveedor.objects.get(rut_proveedor=rut).nombre_proveedor
            lista = Proveedor.listar_op_proveedor(rut)
            return render(
                request,
                'Usuarios/consulta_proveedores.html',
                {'proveedor': proveedor, 'lista': lista})

        except ObjectDoesNotExist:
            return render(request, 'Usuarios/index.html', {'prov_no_registrado': True})
    else:
        return redirect('index')


def detalle_op(request, id_op):
    orden_pedido = OrdenPedido.objects.get(id_orden_pedido=id_op)
    productos = DetalleOrdenPedido.objects.filter(id_orden_pedido=id_op)
    return render(request, 'Usuarios/detalle_op.html', {'orden_pedido': orden_pedido, 'productos': productos})
