# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't
# rename db_table values or field names.
from django.db import models
from Usuarios.models import Empleado


class FamiliaProducto(models.Model):
    id_familia = models.IntegerField(primary_key=True)
    descripcion_familia = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion_familia

    class Meta:
        db_table = 'familia_producto'


class TipoProducto(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    descripcion_tipo = models.CharField(max_length=50)
    id_familia = models.ForeignKey(
        FamiliaProducto, on_delete=models.PROTECT, db_column='id_familia')

    def __str__(self):
        return self.descripcion_tipo

    class Meta:
        db_table = 'tipo_producto'


class Proveedor(models.Model):
    rut_proveedor = models.CharField(primary_key=True, max_length=10)
    nombre_proveedor = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_proveedor

    def listar_op_proveedor(rut):
        return OrdenPedido.objects.filter(rut_proveedor=rut)

    class Meta:
        db_table = 'proveedor'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    fecha_vencimiento = models.DateField()
    descripcion_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    stock_critico_producto = models.IntegerField()
    rut_proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, db_column='rut_proveedor')

    def cmb_familias_tipos(self):
        familias = FamiliaProducto.objects.order_by('descripcion_familia')
        lista_familias = []
        for familia in familias:
            tipos = TipoProducto.objects.order_by('descripcion_tipo').filter(id_familia=familia)
            lista_tipos = []
            for tipo in tipos:
                lista_tipos.append(tipo.descripcion_tipo)
            dic_familia = {
                "familia": familia.descripcion_familia,
                "tipos": lista_tipos
            }
            lista_familias.append(dic_familia)
        return lista_familias

    # (?)
    def generar_id(self, familia, tipo):
        id_concatenado = self.rut_proveedor[:-2] + str(familia) + str(tipo)
        try:
            id_generado = int(id_concatenado)
        except ValueError:
            print("La cadena de caracteres no pudo convertirse en un número.")
        return id_generado

    def __str__(self):
        return self.descripcion_producto

    class Meta:
        db_table = 'producto'


class OrdenPedido(models.Model):
    id_orden_pedido = models.AutoField(primary_key=True)
    suma_precio = models.IntegerField()
    enviada = models.BooleanField(default=0)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)
    rut_proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT, db_column='rut_proveedor')
    id_empleado = models.ForeignKey(
        Empleado, on_delete=models.PROTECT, db_column='id_empleado')

    def __str__(self):
        return str(self.id_orden_pedido)

    class Meta:
        db_table = 'orden_pedido'


class DetalleOrdenPedido(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio_individual = models.IntegerField()
    precio_total = models.IntegerField()
    id_orden_pedido = models.ForeignKey(
        OrdenPedido, on_delete=models.CASCADE, db_column='id_orden_pedido')
    id_producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, db_column='id_producto')

    def __str__(self):
        return str(self.id_orden_pedido) + ' ' + str(self.id_producto)

    class Meta:
        db_table = 'detalle_orden_pedido'


class ServiciosComedor(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        db_table = 'servicios_comedor'


class Platos(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio_plato = models.IntegerField()
    id_servicio = models.ForeignKey(
        ServiciosComedor, on_delete=models.CASCADE, db_column='id_servicio')

    def __str__(self):
        return self.nombre_plato

    class Meta:
        db_table = 'platos'
