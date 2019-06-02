# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from django import forms
from apps.egresados.models import Egresado


class inscripcionFormEgresados(forms.ModelForm):
    class Meta:
        model = Egresado
        
        fields = [
            'identificacion', 'nombre', 'email', 'telefono', 'programa', 'evento'
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre':         'Nombre',
            'email':          'Email',
            'telefono':       'Teléfono',
            'programa':       'Programa Académico',
            'evento':         'Evento'
        }
        
        widgets = {
            'identificacion': forms.TextInput(attrs = {'class': 'form-control'}),
            'nombre':         forms.TextInput(attrs = {'class': 'form-control'}),
            'email':          forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono':       forms.TextInput(attrs = {'class': 'form-control'}),
            'programa':       forms.CheckboxSelectMultiple(),  # forms.Select(attrs = {'class': 'form-control'}),
            'evento':         forms.CheckboxSelectMultiple(),
        }