# Generated by Django 3.2.3 on 2021-05-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negocio', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huesped',
            name='fecha_recepcion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='fecha_orden_compra',
            field=models.DateTimeField(),
        ),
    ]