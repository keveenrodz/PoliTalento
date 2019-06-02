# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from django import forms
#from apps.liderAutoevaluacion.models import
from django import forms
from apps.liderAutoevaluacion.models import Evento


class liderAutoevaluacionFormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        
        fields = [
            'identificacion', 'nombreEvento', 'fecha', 'lugar', 'liderAutoevaluacion'
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombreEvento': 'Nombre del Evento',
            'fecha': 'Fecha',
            'lugar': 'Lugar',
            'liderAutoevaluacion': 'Lider Autoevaluación'
        }
        
        widgets = {
            'identificacion': forms.TextInput(attrs = {'class': 'form-control'}),
            'nombreEvento': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha': forms.DateInput(),
            'lugar': forms.TextInput(attrs = {'class': 'form-control'}),
            'liderAutoevaluacion': forms.Select(attrs = {'class': 'form-control'}),
        }
