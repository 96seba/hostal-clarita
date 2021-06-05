from Servicios.models import OrdenPedido
from django.shortcuts import redirect, render


def listar_ordenes(request):
    orden_pedido = OrdenPedido.objects.all()
    return render(request, "Servicios/listar_ordenes.html", {'orden_pedido': orden_pedido})


def borrar_orden(request, id_orden_pedido):
    borrar = OrdenPedido.objects.get(id_orden_pedido=id_orden_pedido)
    borrar.delete()
    return redirect('listar_ordenes')
