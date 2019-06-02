# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from django.urls import path, re_path
from apps.egresados.views import index
from apps.liderAutoevaluacion.views import EventoList
from apps.egresados.views import InscripcionCreate
from apps.egresados.views import RegistroUsuario

urlpatterns = [
    re_path('^index$', index),
    re_path(r'^listarevento$', EventoList.as_view(), name='evento_listar'),
    re_path(r'^inscripcion$', InscripcionCreate.as_view(), name = 'inscripcion_evento'),
    re_path(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
]