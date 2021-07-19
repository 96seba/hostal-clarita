from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.core.exceptions import ObjectDoesNotExist
from Usuarios.models import Roles
from Usuarios.forms import FormularioUsuario, FormularioCliente
from .models import OrdenDeCompra, Huesped, Factura, Habitacion
from .forms import FormularioOrdenCompra, FormulariosHuespedes, FormularioHabitacion


PRECIO_HABITACION = [
    ('individual', 12990),
    ('doble', 15990),
    ('ejecutiva', 19990),
]


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
            form_usuario = FormularioUsuario(request.POST)
            form_cliente = FormularioCliente(request.POST)
    else:
        form_usuario = FormularioUsuario()
        form_cliente = FormularioCliente()
    return render(
        request,
        'Negocio/registro_cliente.html',
        {'form_usuario': form_usuario, 'form_cliente': form_cliente})


def listar_ordenes_compra(request):
    # recuperar el rut del cliente actualmente logueado
    rut_usuario = request.user.cliente.rut_cliente
    # recuperar todas las OC de ese cliente                       # de la más nueva a la más antigua
    lista_oc = OrdenDeCompra.objects.filter(rut_cliente=rut_usuario).order_by('-fecha_orden_compra')
    # enviarlas a la vista
    return render(request, 'Negocio/lista_orden_compra.html', {'lista_oc': lista_oc})


def registro_orden_compra(request):
    if request.method == 'POST':
        datos_oc = FormularioOrdenCompra(request.POST)
        lista_huespedes = FormulariosHuespedes(request.POST)
        if datos_oc.is_valid() and lista_huespedes.is_valid():
            nueva_oc = datos_oc.save(commit=False)
            nuevos_huespedes = lista_huespedes.save(commit=False)
            nueva_oc.rut_cliente = request.user.cliente
            nueva_oc.cantidad_huespedes = len(nuevos_huespedes)
            nueva_oc.save()
            for huesped in nuevos_huespedes:
                huesped.id_orden_compra = nueva_oc
                huesped.save()
            return redirect('listar_ordenes_compra')
        else:
            form_oc = FormularioOrdenCompra(request.POST)
            form_huespedes = FormulariosHuespedes(request.POST)
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
        OrdenDeCompra, Huesped, fields=('nombre_huesped',), min_num=1, validate_min=True, extra=0)
    # recibe las actualizaciónes de datos
    if request.method == 'POST':
        datos_orden = FormularioOrdenCompra(request.POST, instance=orden)
        datos_huespedes = huespedes(request.POST, instance=orden)
        if datos_orden.is_valid() and datos_huespedes.is_valid():
            orden_actualizada = datos_orden.save(commit=False)
            orden_actualizada.cantidad_huespedes = datos_huespedes.total_form_count()
            orden_actualizada.save()
            datos_huespedes.save()
        else:
            form_oc = FormularioOrdenCompra(request.POST)
            form_huespedes = huespedes(request.POST)
    # prellena los formularios con los datos
    form_oc = FormularioOrdenCompra(instance=orden)
    form_huespedes = huespedes(instance=orden)
    return render(
        request,
        'Negocio/editar_orden_compra.html',
        {
            'orden': orden,
            'form_oc': form_oc,
            'form_huespedes': form_huespedes,
            'tiene_factura': orden.tiene_factura(orden.id_orden_compra)
        }
    )


def eliminar_orden_compra(request, oc_id):
    orden = OrdenDeCompra.objects.get(id_orden_compra=oc_id)
    orden.delete()
    return redirect('listar_ordenes_compra')


def generar_factura(request, oc_id):
    orden = OrdenDeCompra.objects.get(id_orden_compra=oc_id)
    precio_habitacion = 0
    for habitacion in PRECIO_HABITACION:
        if habitacion[0] == orden.tipos_habitacion:
            precio_habitacion = habitacion[1]
    total = orden.cantidad_huespedes * precio_habitacion
    nueva_factura = Factura(id_orden_compra=orden, total=total, estado_factura=1)
    nueva_factura.save()
    return redirect('listar_facturas')


def listar_facturas(request):
    rut_cliente = request.user.cliente.rut_cliente
    ordenes_compra = OrdenDeCompra.objects.filter(rut_cliente=rut_cliente)
    facturas = []
    ordenes_no_facturadas = []
    for orden in ordenes_compra:
        try:
            factura = Factura.objects.get(id_orden_compra=orden.id_orden_compra)
            facturas.append(factura)
        except ObjectDoesNotExist:
            ordenes_no_facturadas.append(orden)
    return render(request, 'Negocio/lista_facturas.html', {'facturas': facturas})


def detalle_factura(request, id_factura):
    factura = Factura.objects.get(nro_factura=id_factura)
    huespedes = factura.id_orden_compra.obtener_huespedes(
        factura.id_orden_compra.id_orden_compra)
    ###
    for habitacion in PRECIO_HABITACION:
        if habitacion[0] == factura.id_orden_compra.tipos_habitacion:
            precio_habitacion = habitacion[1]
    return render(
        request,
        'Negocio/detalle_factura.html',
        {'factura': factura, 'huespedes': huespedes, 'precio_habitacion': precio_habitacion}
    )


def anular_factura(request, id_factura):
    factura = Factura.objects.get(nro_factura=id_factura)
    factura.delete()
    return redirect('listar_facturas')


def registro_habitacion(request):
    if request.method == 'POST':
        datos_habitacion = FormularioHabitacion(request.POST)
        if datos_habitacion.is_valid():
            nueva_habitacion = datos_habitacion.save(commit=False)
            nueva_habitacion.save()
            return redirect('listar_habitacion')
        else:
            form_habitacion = FormularioHabitacion(request.POST)
    else:
        form_habitacion = FormularioHabitacion()
    return render(
        request,
        'Negocio/registro_habitacion.html',
        {'form_habitacion': form_habitacion})


def listar_habitacion(request):
    lista_h = Habitacion.objects.all()
    return render(request, "Negocio/listar_habitacion.html", {'lista_h': lista_h})
