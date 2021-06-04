from django import forms
from .models import OrdenDeCompra, Huesped


class FormularioOrdenCompra(forms.ModelForm):
    class Meta:
        model = OrdenDeCompra
        fields = [
            'servicios_contratados',
            'tipos_habitacion'
        ]
        labels = {
            'servicios_contratados': 'Servicios contratados',
            'tipos_habitacion': 'Tipo de habitación',
        }


class FormularioHuesped(forms.ModelForm):
    class Meta:
        model = Huesped
        fields = [
            'nombre_huesped'
        ]
        labels = {
            'nombre_huesped': 'Nombre',
        }


FormulariosHuespedes = forms.modelformset_factory(
    Huesped,
    fields=('nombre_huesped',),
    extra=0,
    labels={'nombre_huesped': 'Nombre'},
    min_num=1,
    validate_min=True
)
