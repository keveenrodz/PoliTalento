# Generated by Django 2.2.1 on 2019-05-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liderAutoevaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombreEvento',
            field=models.CharField(max_length=100),
        ),
    ]
