# Generated by Django 3.2.3 on 2021-05-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20210518_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_cliente',
            field=models.BooleanField(default=1),
        ),
    ]
