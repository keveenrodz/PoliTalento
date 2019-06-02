# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from django.urls import path, re_path
from apps.liderAutoevaluacion.views import index
from apps.liderAutoevaluacion.views import liderAutoevaluacion_viewEvento
from apps.liderAutoevaluacion.views import EventoList
from apps.liderAutoevaluacion.views import EventoCreate
from apps.liderAutoevaluacion.views import EventoUpdate
from apps.liderAutoevaluacion.views import EventoDelete
from apps.administrador.views import EgresadoList

urlpatterns = [
    re_path('^index$', index, name='index'),
    re_path(r'^nuevoevento$', EventoCreate.as_view(), name='evento_crear'),
    re_path(r'^listarevento$', EventoList.as_view(), name='evento_listar'),
    re_path(r'^editarevento/(?P<pk>\d+)/$', EventoUpdate.as_view(), name='evento_editar'),
    re_path(r'^eliminarevento/(?P<pk>\d+)/$', EventoDelete.as_view(), name='evento_eliminar'),
    re_path(r'^listaregresado$', EgresadoList.as_view(), name = 'egresado_listar'),
    
]