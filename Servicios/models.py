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


class Proveedor(models.Model):
    rut_proveedor = models.CharField(primary_key=True, max_length=10)
    nombre_proveedor = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_proveedor

    def listar_op_proveedor(rut):
        # recuperar todos los productos de un mismo proveedor
        productos = Producto.objects.filter(rut_proveedor=rut)
        # crear una lista vacía...
        op = []
        for producto in productos:
            # recorrer todos los productos para buscar
            # todas las OP que los contengan
            lista = DetalleOrdenPedido.objects.filter(
                id_producto=producto.id_producto)
            # e ir almacenandolos en la lista
            for detalle in lista:
                op.append(detalle)
        return op

    class Meta:
        db_table = 'proveedor'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    familia_producto = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    tipo_producto = models.IntegerField()
    descripcion_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    stock_critico_producto = models.IntegerField()
    rut_proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, db_column='rut_proveedor')

    def __str__(self):
        return self.descripcion_producto

    class Meta:
        db_table = 'producto'


class OrdenPedido(models.Model):
    id_orden_pedido = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    suma_precio = models.IntegerField()
    fecha_recepcion = models.DateField(blank=True, null=True)
    id_empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, db_column='id_empleado')

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
