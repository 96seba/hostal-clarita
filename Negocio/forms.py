from django import forms
from .models import OrdenDeCompra


class FormularioOrdenCompra(forms.ModelForm):
    class Meta:
        model = OrdenDeCompra
        fields = [
            'servicios_contratados',
            'cantidad_huespedes',
            'tipos_habitacion'
        ]
        labels = {
            'servicios_contratados': 'Servicios contratados',
            'cantidad_huespedes': 'Cantidad de huéspedes',
            'tipos_habitacion': 'Tipo de habitación',
        }
