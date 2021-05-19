from django.contrib import admin
from .models import Habitacion, OrdenDeCompra, Huesped, Factura

admin.site.register(Habitacion)
admin.site.register(OrdenDeCompra)
admin.site.register(Huesped)
admin.site.register(Factura)
