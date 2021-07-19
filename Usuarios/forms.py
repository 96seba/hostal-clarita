from django import forms
from .models import Usuario, Cliente, Empleado
from django.contrib.auth.forms import UserCreationForm


class FormularioUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']
        labels = {
            'username': 'Usuario',
            'email': 'Correo',
        }


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
            'rut_cliente': forms.TextInput(attrs={'placeholder': 'Ej.: 12345678-K', 'oninput': 'checkRut(this)'}),
            'nombre_empresa': forms.TextInput(),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej.: 987654321'}),
        }


class FormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'id_empleado',
            'nombre_empleado',
            'rut_empleado',
            'cargo_empleado',
            'telefono',
            'direccion'
        ]
        labels = {
            'id_empleado': 'ID Empleado',
            'nombre_empleado': 'Nombre',
            'rut_empleado': 'RUT',
            'cargo_empleado': 'Cargo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            
        }
