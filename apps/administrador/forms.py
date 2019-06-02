# Author: Keveen Rodriguez Zapata <keveenrodriguez@gmail.com>
#
# License: GNU Lesser General Public License v3.0 (LGPLv3)
from django import forms
from apps.administrador.models import Programa
from apps.egresados.models import Egresado
from apps.administrador.models import Administrador
from apps.liderAutoevaluacion.models import LiderAutoevaluacion


class AdministradorFormPrograma(forms.ModelForm):
    
    class Meta:
        model = Programa
        
        fields = [
            'codigoRegCalificado', 'nombrePrograma', 'duracion', 'perfil', 'estadoActual'
        ]
        labels = {
            'codigoRegCalificado' : 'Codigo Registro Calificado',
            'nombrePrograma' : 'Nombre Programa',
            'duracion' : 'Duracion',
            'perfil' : 'Perfil',
            'estadoActual' : 'Estado Actual'
        }
        
        widgets = {
            'codigoRegCalificado': forms.TextInput(attrs = {'class': 'form-control'}),
            'nombrePrograma': forms.TextInput(attrs = {'class': 'form-control'}),
            'duracion': forms.TextInput(attrs = {'class': 'form-control'}),
            'perfil': forms.TextInput(attrs = {'class': 'form-control'}),
            'estadoActual': forms.TextInput(attrs = {'class': 'form-control'}),
        }


class AdministradorFormEgresados(forms.ModelForm):
    class Meta:
        model = Egresado

        fields = [
            'identificacion', 'nombre', 'email', 'telefono', 'contrasena', 'programa', 'administrador'
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre' : 'Nombre',
            'email' : 'Email',
            'telefono' : 'Teléfono',
            'contrasena': 'Contraseña',
            'programa': 'Programa Académico',
            'administrador': 'Administrador'
        }
        
        widgets = {
            'identificacion':  forms.TextInput(attrs = {'class': 'form-control'}),
            'nombre' : forms.TextInput(attrs = {'class': 'form-control'}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs = {'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'autocomplete': 'off','class': 'form-control', }),
            'programa': forms.CheckboxSelectMultiple(),  #forms.Select(attrs = {'class': 'form-control'}),
            'administrador': forms.Select(attrs = {'class': 'form-control'}),
        }


class AdministradorFormAdministrador(forms.ModelForm):
    class Meta:
        model = Administrador
        
        fields = [
            'identificacion', 'nombre', 'email', 'telefono', 'contrasena'
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre':         'Nombre',
            'email':          'Email',
            'telefono':       'Teléfono',
            'contrasena':     'Contraseña',
        }

        widgets = {
            'identificacion' : forms.TextInput(attrs = {'class': 'form-control'}),
            'nombre' : forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs = {'class': 'form-control'}),
            'contrasena' : forms.TextInput(attrs = {'class': 'form-control'}),
        }


class AdministradorFormliderAutoevaluacion(forms.ModelForm):
    class Meta:
        model = LiderAutoevaluacion
        
        fields = [
            'identificacion', 'nombre', 'email', 'telefono', 'contrasena', 'programa'
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre': 'Nombre',
            'email': 'Email',
            'telefono': 'Teléfono',
            'contrasena': 'Contraseña',
            'programa' : 'Programa',
        }
        
        widgets = {
            'identificacion': forms.TextInput(attrs = {'class': 'form-control'}),
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'autocomplete': 'off','class': 'form-control', }),
            'programa': forms.Select(attrs = {'class': 'form-control'}),
        }