from Servicios.models import OrdenPedido
from django.shortcuts import redirect, render
from .forms import OrdenPedidoForm


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
        form = OrdenPedidoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listar_ordenes')
    else:
        form = OrdenPedidoForm()
    return render(request, 'Servicios/registro_ordenCompra.html', {'form': form})
