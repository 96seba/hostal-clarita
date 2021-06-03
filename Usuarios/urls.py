from django.urls import path
from .views import index, consulta_proveedores

urlpatterns = [
    path('', index, name='index'),
    path('proveedores/', consulta_proveedores, name='consulta_proveedores'),
]
