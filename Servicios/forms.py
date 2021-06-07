from django import forms
from .models import (OrdenPedido, DetalleOrdenPedido, Platos, ServiciosComedor)


class OrdenPedidoForm(forms.ModelForm):
    class Meta:
        model = OrdenPedido
        fields = ['id_orden_pedido',
                  'suma_precio',
                  'observaciones',
                  'rut_proveedor']
        labels = {
            'id_orden_pedido': 'Id Orden de pedido',
            'suma_precio': 'Suma de precios',
            'observaciones': 'Observaciones',
            'rut_proveedor': 'Proveedor',
        }
        widgets = {
            'id_orden_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'suma_precio': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }


class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = DetalleOrdenPedido
        fields = ['id',
                  'id_producto',
                  'cantidad',
                  'precio_individual',
                  'precio_total']
        labels = {
            'id': 'Id Orden de pedido',
            'id_producto': 'Producto',
            'cantidad': 'Cantidad',
            'precio_individual': 'Precio unitario',
            'precio_total': 'Precio total',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_individual': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_total': forms.TextInput(attrs={'class': 'form-control'}),
            }


DetallesForm = forms.modelformset_factory(
    DetalleOrdenPedido,
    fields=('id',
            'id_producto',
            'cantidad',
            'precio_individual',
            'precio_total',),
    extra=0,
    labels={'id': 'Id Orden de pedido',
            'id_producto': 'Producto',
            'cantidad': 'Cantidad',
            'precio_individual': 'Precio unitario',
            'precio_total': 'Precio total'},
    min_num=1,
    validate_min=True
)


class FormularioPlatos(forms.ModelForm):
    class Meta:
        model = Platos 
        fields = [
            'id_plato',
            'nombre_plato',
            'descripcion',
            'precio_plato',
            'id_servicio'
        ]
        labels = {
            'id_plato' : 'ID Plato',
            'nombre_plato' : 'Nombre del plato',
            'descripcion' : 'Descripcion plato',
            'precio_plato' : 'Precio plato',
            'id_servicio' : 'ID servicio', 
        }
        widgets = {
            'id_plato': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_plato': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_plato': forms.TextInput(attrs={'class': 'form-control'}),
            'id_servicio': forms.Select(attrs={'class': 'form-control'}),
        }
        


class FormularioServiciosComedor(forms.ModelForm):
    class Meta:
        model = ServiciosComedor
        fields = [
            'id_servicio',
            'nombre_servicio',
            'descripcion'
        ]
        labels = {
            'id_servicio': 'ID Servicio',
            'nombre_servicio': 'Nombre servicio',
            'descripcion' : 'Descripcion servicio',
        }

