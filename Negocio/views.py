from django.shortcuts import render, redirect
from Usuarios.models import Roles
from Usuarios.forms import FormularioUsuario, FormularioCliente
# from .models import OrdenDeCompra
from .forms import FormularioOrdenCompra


def registro_cliente(request):
    if request.method == 'POST':
        datos_usuario = FormularioUsuario(request.POST)
        datos_cliente = FormularioCliente(request.POST)
        if datos_usuario.is_valid() and datos_cliente.is_valid():
            # guardar y manipular los datos del nuevo usuario
            nuevo_usuario = datos_usuario.save(commit=False)
            nuevo_usuario.id_rol = Roles.objects.get(id_rol=3)
            # guardar y manipular los datos del nuevo cliente
            nuevo_cliente = datos_cliente.save(commit=False)
            nuevo_cliente.usuario = nuevo_usuario
            # almacenar los datos
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
    rut = request.user.email
    print(rut)
    # recuperar todas las OC de ese cliente
    # enviarlas a la vista
    return render(request, 'Negocio/lista_orden_compra.html')


def registro_orden_compra(request):
    if request.method == 'POST':
        pass
    else:
        form_oc = FormularioOrdenCompra()
    return render(request, 'Negocio/registro_orden_compra.html', {'form_oc': form_oc})
