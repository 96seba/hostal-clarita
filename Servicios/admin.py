from django.contrib import admin
from .models import ServiciosComedor, Platos, Proveedor, Producto, OrdenPedido, DetalleOrdenPedido

admin.site.register(ServiciosComedor)
admin.site.register(Platos)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(OrdenPedido)
admin.site.register(DetalleOrdenPedido)
