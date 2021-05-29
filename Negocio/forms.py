from django import forms
from Usuarios.models import Cliente, Usuario
from django.contrib.auth.forms import UserCreationForm


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut_cliente', 'nombre_empresa', 'telefono']
        labels = {
            'rut_cliente': 'RUT',
            'nombre_empresa': 'Nombre de empresa',
            'telefono': 'Teléfono',
        }
        widgets = {
            'rut_cliente': forms.TextInput(),
            'nombre_empresa': forms.TextInput(),
            'telefono': forms.TextInput(),
        }


class FormularioUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']
        labels = {
            'username': 'Usuario',
            'email': 'Correo',
        }
