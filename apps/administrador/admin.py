from django.contrib import admin
from apps.administrador.models import Programa

from apps.liderAutoevaluacion.models import LiderAutoevaluacion
from apps.egresados.models import Egresado
from apps.administrador.models import Administrador

# Register your models here.

admin.site.register(LiderAutoevaluacion)
admin.site.register(Programa)
admin.site.register(Egresado)
admin.site.register(Administrador)

