from Servicios.models import DetalleOrdenPedido, OrdenPedido
from django.shortcuts import redirect, render
from .forms import (DetallesForm, OrdenPedidoForm)


def listar_ordenes(request):
    orden_pedido = OrdenPedido.objects.all()
    return render(request, "Servicios/listar_ordenes.html", {'orden_pedido': orden_pedido})


def borrar_orden(request, id_orden_pedido):
    borrar = OrdenPedido.objects.get(id_orden_pedido=id_orden_pedido)
    borrar.delete()
    return redirect('listar_ordenes')


def cmb_ordenes(request):
    orden_pedido = OrdenPedido.objects.all()
    return render(request, "Servicios/recepcion_productos.html", {'orden_pedido': orden_pedido})


def generar_ordenPedido(request):
    if request.method == 'POST':
        datos_op = OrdenPedidoForm(request.POST)
        detalle = DetallesForm(request.POST)
        if datos_op.is_valid() and detalle.is_valid():
            nueva_op = datos_op.save(commit=False)
            nuevos_detalles = detalle.save(commit=False)
            nueva_op.id_empleado = request.user.empleado
            nueva_op.save()
            for dop in nuevos_detalles:
                dop.id_orden_pedido = nueva_op
                dop.save()
            return redirect('listar_ordenes')
        else:
            form_op = OrdenPedidoForm(request.POST)
            form_detalle = DetallesForm(request.POST)
    else:
        form_op = OrdenPedidoForm()
        form_detalle = DetallesForm(queryset=DetalleOrdenPedido.objects.none())
    return render(
        request,
        'Servicios/registro_ordenCompra.html',
        {'form_op': form_op, 'form_detalle': form_detalle})
