from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Roles, Usuario, Cliente, Empleado

admin.site.register(Roles)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Cliente)
admin.site.register(Empleado)
