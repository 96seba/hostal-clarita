from django.shortcuts import render, redirect
from Usuarios.models import Roles
from Usuarios.forms import FormularioUsuario, FormularioCliente
from .models import OrdenDeCompra, Huesped
from .forms import FormularioOrdenCompra, FormulariosHuespedes
from django.forms import inlineformset_factory


def registro_cliente(request):
    if request.method == 'POST':
        datos_usuario = FormularioUsuario(request.POST)
        datos_cliente = FormularioCliente(request.POST)
        if datos_usuario.is_valid() and datos_cliente.is_valid():
            # guarda en un objeto y manipula los datos del nuevo usuario
            nuevo_usuario = datos_usuario.save(commit=False)
            nuevo_usuario.id_rol = Roles.objects.get(id_rol=3)
            # guarda en un objeto y manipula los datos del nuevo cliente
            nuevo_cliente = datos_cliente.save(commit=False)
            nuevo_cliente.usuario = nuevo_usuario
            # almacena los objetos en la base de datos
            nuevo_usuario.save()
            nuevo_cliente.save()
            return redirect('index')
    else:
        datos_usuario = FormularioUsuario()
        datos_cliente = FormularioCliente()
    return render(
        request,
        'Negocio/registro_cliente.html',
        {'datos_usuario': datos_usuario, 'datos_cliente': datos_cliente})


def listar_ordenes_compra(request):
    # recuperar el rut del cliente actualmente logueado
    rut_usuario = request.user.cliente.rut_cliente
    # recuperar todas las OC de ese cliente                       # de la más nueva a la más antigua
    lista_oc = OrdenDeCompra.objects.filter(rut_cliente=rut_usuario).order_by('-fecha_orden_compra')
    # enviarlas a la vista
    for oc in lista_oc:
        print(oc)
    return render(request, 'Negocio/lista_orden_compra.html', {'lista_oc': lista_oc})


def registro_orden_compra(request):
    if request.method == 'POST':
        datos_oc = FormularioOrdenCompra(request.POST)
        lista_huespedes = FormulariosHuespedes(data=request.POST)
        if datos_oc.is_valid() and lista_huespedes.is_valid():
            # almacena los datos de los formularios en objetos
            # para después añadirle los atributos faltantes
            nueva_oc = datos_oc.save(commit=False)
            nuevos_huespedes = lista_huespedes.save(commit=False)
            # añade la referencia al cliente y el total de huespedes
            # a la OC almacena la oc en la base de datos
            nueva_oc.rut_cliente = request.user.cliente
            nueva_oc.cantidad_huespedes = lista_huespedes.total_form_count()
            nueva_oc.save()
            # añade la referencia a la OC a cada huesped
            # y almacenarlos en la base de datos
            for huesped in nuevos_huespedes:
                huesped.id_orden_compra = nueva_oc
                huesped.save()
            return redirect('listar_ordenes_compra')
    else:
        form_oc = FormularioOrdenCompra()
        form_huespedes = FormulariosHuespedes(queryset=Huesped.objects.none())
    return render(
        request,
        'Negocio/registro_orden_compra.html',
        {'form_oc': form_oc, 'form_huespedes': form_huespedes}
    )


def editar_orden_compra(request, oc_id):
    # recupera la orden y todos sus huéspedes asociados
    orden = OrdenDeCompra.objects.get(id_orden_compra=oc_id)
    huespedes = inlineformset_factory(
        OrdenDeCompra, Huesped, fields=('nombre_huesped',), extra=0)

    # recibe las actualizaciónes de datos
    if request.method == 'POST':
        datos_orden = FormularioOrdenCompra(request.POST, instance=orden)
        datos_huespedes = huespedes(request.POST, instance=orden)

        if datos_orden.is_valid():
            datos_orden.save()
            # actualizacion_orden = datos_orden.save(commit=False)
            # actualizacion_orden.save()
        if datos_huespedes.is_valid():
            datos_huespedes.save()
        else:
            print("/////////////pare que hubo un atao/////////////")
            print(datos_huespedes)

    # else:
    # prellena los formularios con los datos
    form_orden = FormularioOrdenCompra(instance=orden)
    # form_huespedes = FormulariosHuespedes(queryset=Huesped.objects.filter(id_orden_compra=oc_id))
    form_huespedes = huespedes(instance=orden)

    return render(
        request,
        'Negocio/editar_orden_compra.html',
        {
            'orden': orden,
            'form_orden': form_orden,
            'form_huespedes': form_huespedes
        }
    )


def eliminar_orden_compra(request, oc_id):
    orden = OrdenDeCompra.objects.get(id_orden_compra=oc_id)
    orden.delete()
    return redirect('listar_ordenes_compra')
