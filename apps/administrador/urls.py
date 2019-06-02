# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from django.urls import path, re_path
from apps.administrador.views import index
#from apps.administrador.views import administrador_viewPrograma
from apps.administrador.views import administrador_viewEgresados
from apps.administrador.views import administrador_viewAdministrador
from apps.administrador.views import administrador_viewliderAutoevaluacion
#from apps.administrador.views import programas_list # Lista basada en funciones
#from apps.administrador.views import programas_edit
#from apps.administrador.views import programas_delete
from apps.administrador.views import ProgramaList # Lista basada en clases
from apps.administrador.views import ProgramaCreate # Crear basada en clases
from apps.administrador.views import ProgramaUpdate # Actualizar basada en clases
from apps.administrador.views import ProgramaDelete # Eliminar basada en clases
from apps.administrador.views import EgresadoList
from apps.administrador.views import EgresadoCreate
from apps.administrador.views import EgresadoUpdate
from apps.administrador.views import EgresadoDelete





from django.conf.urls import url, include

urlpatterns = [
    re_path('^index$', index, name = 'index'),
    re_path(r'^nuevoprograma$', ProgramaCreate.as_view(), name = 'administrador_crearPrograma'),#re_path('^nuevoprograma$', administrador_viewPrograma, name = 'administrador_crearPrograma'),
    re_path(r'^nuevoegresado$', EgresadoCreate.as_view(), name = 'administrador_crearEgresado'),
    re_path('^nuevoadministrador$', administrador_viewAdministrador, name = 'administrador_crearAdministrador'),
    re_path('^nuevoliderAutoevaluacion$', administrador_viewliderAutoevaluacion,
            name = 'administrador_crearliderAutoevaluacion'),
    re_path('^listarprograma$', ProgramaList.as_view(), name = 'programa_listar'),#re_path('^listarprograma$', programas_list, name = 'programa_listar'),
    re_path(r'^editarprograma/(?P<pk>\d+)/$', ProgramaUpdate.as_view(), name = 'programa_editar'),#re_path(r'^editarprograma/(?P<codigoRegCalificado>\d+)/$', programas_edit, name = 'programa_editar'),
    re_path(r'^eliminarprograma/(?P<pk>\d+)/$', ProgramaDelete.as_view(), name = 'programa_eliminar'),#re_path(r'^eliminarprograma/(?P<codigoRegCalificado>\d+)/$', programas_delete, name = 'programa_eliminar'),
    re_path(r'^listaregresado$', EgresadoList.as_view(), name = 'egresado_listar'),
    re_path(r'^editaregresado/(?P<pk>\d+)/$', EgresadoUpdate.as_view(), name = 'egresado_editar'),
    re_path(r'^eliminaregresado/(?P<pk>\d+)/$', EgresadoDelete.as_view(), name = 'egresado_eliminar'),
]
