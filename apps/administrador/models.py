from django.db import models
# Create your models here.

class Administrador(models.Model):
    identificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    contrasena = models.CharField(max_length=20)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Programa(models.Model):
    codigoRegCalificado = models.CharField(primary_key=True, max_length=40)
    nombrePrograma = models.CharField(max_length=50)
    duracion = models.IntegerField()
    perfil = models.CharField(max_length=30)
    estadoActual = models.SmallIntegerField()
    
    def __str__(self):
        return '{}'.format(self.nombrePrograma)
    

