from django.db import models

# Create your models here.
from apps.administrador.models import Programa


class LiderAutoevaluacion(models.Model):
    identificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    contrasena = models.CharField(max_length=20)
    programa = models.ForeignKey(Programa, null = True, blank = True, on_delete = models.CASCADE)


class Evento(models.Model):
    identificacion = models.CharField(primary_key = True, max_length = 30)
    nombreEvento = models.CharField(max_length = 100)  # Field name made lowercase.
    fecha = models.DateField()
    lugar = models.CharField(max_length = 30)
    liderAutoevaluacion = models.ForeignKey(LiderAutoevaluacion, null = False, blank = False, on_delete = models.CASCADE)
    

class Organizador(models.Model):
    identificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    evento = models.ForeignKey(Evento, null = False, blank = False, on_delete = models.CASCADE)