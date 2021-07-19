from django import forms
from .models import OrdenDeCompra, Huesped, Habitacion


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


class FormularioHabitacion(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['nro_habitacion',
                  'estado_habitacion',
                  'tipo_cama',
                  'accesorios_habitacion',
                  'precio_habitacion']
        labels = {
            'nro_habitacion': 'Numero de habitacion',
            'estado_habitacion': 'Estado de habitacion',
            'tipo_cama': 'Tipo de cama',
            'accesorios_habitacion': 'Accesorios de habitacion',
            'precio_habitacion': 'Precio de habitacion',
        }
        widgets = {
            'nro_habitacion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_habitacion': forms.Select(attrs={'class': 'form-control'}),
            'tipo_cama': forms.Select(attrs={'class': 'form-control'}),
            'accesorios_habitacion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_habitacion': forms.TextInput(attrs={'class': 'form-control'}),
        }
