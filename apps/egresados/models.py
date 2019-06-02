from django.db import models
from apps.administrador.models import Programa
from apps.administrador.models import Administrador
from apps.liderAutoevaluacion.models import Evento



class Egresado(models.Model):
    identificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    contrasena = models.CharField(max_length=20)
    programa = models.ManyToManyField(Programa)
    evento = models.ManyToManyField(Evento)
    administrador = models.ForeignKey(Administrador, null = True, blank = True, on_delete = models.CASCADE)
    