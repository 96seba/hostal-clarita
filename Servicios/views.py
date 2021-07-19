from Servicios.models import DetalleOrdenPedido, OrdenPedido
from django.shortcuts import redirect, render
from .forms import (DetallesForm, OrdenPedidoForm, FormularioServiciosComedor, ServiciosComedor, FormularioPlatos)


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


def listar_detalle_pedido(request, id_orden_pedido):
    detalle_pedido = DetalleOrdenPedido.objects.filter(id_orden_pedido__id_orden_pedido=id_orden_pedido)
    return render(request, "Servicios/listar_detalle_pedidos.html", {'detalle_pedido': detalle_pedido})


def registro_servicio_comedor(request):
    if request.method == 'POST':
        datos_sc = FormularioServiciosComedor(request.POST)
        if datos_sc.is_valid():
            datos_sc.save()
        return redirect('listar_servicio_comedor')
    else:
        datos_sc = FormularioServiciosComedor()
    return render(request, "Servicios/registro_servicios_comedor.html", {'datos_sc': datos_sc})


def listar_servicio_comedor(request):
    servicio_comedor = ServiciosComedor.objects.all()
    return render(request, "Servicios/listar_servicios_comedor.html", {'servicio_comedor': servicio_comedor})


def registro_plato(request):
    if request.method == 'POST':
        datos_pl = FormularioPlatos(request.POST)
        if datos_pl.is_valid():
            datos_pl.save()
        return redirect('listar_servicio_comedor')
    
    else:
        datos_pl = FormularioPlatos()
    return render(request, "Servicios/registro_plato.html", {'datos_pl': datos_pl })