# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=20)
    descripcion_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

    class Meta:
        db_table = 'roles'


class Usuario(AbstractUser):
    id_rol = models.ForeignKey(
        Roles, on_delete=models.PROTECT, db_column='id_rol', default=1)

    @property
    def es_administrador(self):
        if str(self.id_rol) == "Administrador":
            return True

    @property
    def es_empleado(self):
        if str(self.id_rol) == "Empleado":
            return True

    @property
    def es_cliente(self):
        if str(self.id_rol) == "Cliente":
            return True

    class Meta:
        db_table = 'usuario'


class Cliente(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=10)
    nombre_empresa = models.CharField(max_length=50)
    telefono = models.IntegerField()
    estado_cliente = models.BooleanField(default=1)
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        db_table = 'cliente'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=60)
    rut_empleado = models.CharField(max_length=10)
    cargo_empleado = models.CharField(max_length=40)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=60)
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_empleado

    class Meta:
        db_table = 'empleado'
