# Generated by Django 2.2.1 on 2019-05-24 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_remove_administrador_programa'),
        ('egresados', '0003_auto_20190524_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='egresado',
            name='administrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Administrador'),
        ),
    ]
