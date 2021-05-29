from django.shortcuts import render, redirect
from Usuarios.models import Roles
from .forms import FormularioUsuario, FormularioCliente


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
