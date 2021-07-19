from django.shortcuts import render, redirect
from Servicios.models import Proveedor, OrdenPedido, DetalleOrdenPedido, Empleado
from Usuarios.models import Roles
from Usuarios.forms import FormularioUsuario, FormularioEmpleado
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


def registro_empleado(request):
    if request.method == 'POST':
        datos_usuario = FormularioUsuario(request.POST)
        datos_empleado = FormularioEmpleado(request.POST)
        if datos_usuario.is_valid() and datos_empleado.is_valid():
            nuevo_usuario = datos_usuario.save(commit=False)
            nuevo_usuario.id_rol = Roles.objects.get(id_rol=2)
            nuevo_empleado = datos_empleado.save(commit=False)
            nuevo_empleado.usuario = nuevo_usuario
            nuevo_usuario.save()
            nuevo_empleado.save()
            return redirect('index')
        else:
            form_usuario = FormularioUsuario(request.POST)
            form_empleado = FormularioEmpleado(request.POST)
    else:
        form_usuario = FormularioUsuario()
        form_empleado = FormularioEmpleado()
    return render(
        request,
        'Usuarios/registro_empleado.html',
        {'form_usuario': form_usuario, 'form_empleado': form_empleado})


def listar_empleados(request):
    lista_empleado = Empleado.objects.all()
    return render(request, 'Usuarios/listar_empleados.html', {'lista_empleado': lista_empleado})
