from django import forms
from .models import OrdenPedido


class OrdenPedidoForm(forms.ModelForm):
    class Meta:
        model = OrdenPedido
        fields = ['id_orden_pedido',
                  'suma_precio',
                  'observaciones',
                  'rut_proveedor',
                  'id_empleado']

        labels = {
            'id_orden_pedido': 'Id Orden de pedido',
            'suma_precio': 'Suma de precios',
            'observaciones': 'Observaciones',
            'rut_proveedor': 'Rut del proveedor',
            'id_empleado': 'Id del empleado',
        }
        widgets = {
            'id_orden_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'suma_precio': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'id_empleado': forms.Select(attrs={'class': 'form-control'}),
        }
