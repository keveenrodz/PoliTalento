from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponse, request
from apps.administrador.forms import AdministradorFormPrograma
from apps.administrador.forms import AdministradorFormEgresados
from apps.administrador.forms import AdministradorFormAdministrador
from apps.administrador.forms import AdministradorFormliderAutoevaluacion
from apps.administrador.models import Programa
from apps.egresados.models import Egresado


# Create your views here.


def index(request):
    # return HttpResponse("Pagina ppal de administrador")
    return render(request, 'administrador/index.html')


def administrador_viewPrograma(request):
    if request.method == 'POST':
        form = AdministradorFormPrograma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador:index')
    else:
        form = AdministradorFormPrograma()
        
    return render(request, 'administrador/adminForm.html', {'form': form})


def administrador_viewEgresados(request):
    if request.method == 'POST':
        form = AdministradorFormEgresados(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador:index')
    else:
        form = AdministradorFormEgresados()
    
    return render(request, 'administrador/adminFormEgresado.html', {'form': form})


def administrador_viewAdministrador(request):
    if request.method == 'POST':
        form = AdministradorFormAdministrador(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador:index')
    else:
        form = AdministradorFormAdministrador()
    
    return render(request, 'administrador/adminFormAdministrador.html', {'form': form})


def administrador_viewliderAutoevaluacion(request):
    if request.method == 'POST':
        form = AdministradorFormliderAutoevaluacion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador:index')
    else:
        form = AdministradorFormliderAutoevaluacion()
    
    return render(request, 'administrador/adminFormliderAutoevaluacion.html', {'form': form})


def programas_list(request):
    programa = Programa.objects.all().order_by('codigoRegCalificado')
    contexto = {'programas': programa}
    return render(request, 'administrador/programaListar.html', contexto)


def programas_edit(request, codigoRegCalificado):
    programa = Programa.objects.get(codigoRegCalificado=codigoRegCalificado)
    if request.method == 'GET':
        form = AdministradorFormPrograma(instance=programa)
    else:
        form = AdministradorFormPrograma(request.POST, instance=programa)
        if form.is_valid():
            form.save()
        return redirect('administrador:programa_listar')
    return render(request, 'administrador/adminForm.html', {'form': form})


def programas_delete(request, codigoRegCalificado):
    programa = Programa.objects.get(codigoRegCalificado=codigoRegCalificado)
    if request.method == 'POST':
        programa.delete()
        return redirect('administrador:programa_listar')
    return render(request, 'administrador/adminEliminar.html', {'programa': programa})


class ProgramaList(ListView):
    model = Programa
    template_name = 'administrador/programaListar.html'
    

class ProgramaCreate(CreateView):
    model = Programa
    form_class = AdministradorFormPrograma
    template_name = 'administrador/adminForm.html'
    success_url = reverse_lazy('administrador:programa_listar')
    
class ProgramaUpdate(UpdateView):
    model = Programa
    form_class = AdministradorFormPrograma
    template_name = 'administrador/adminForm.html'
    success_url = reverse_lazy('administrador:programa_listar')
    
class ProgramaDelete(DeleteView):
    model = Programa
    template_name = 'administrador/adminEliminar.html'
    success_url = reverse_lazy('administrador:programa_listar')
    
class EgresadoList(ListView):
    model = Egresado
    template_name = 'administrador/egresadoListar.html'
    
class EgresadoCreate(CreateView):
    model = Egresado
    form_class = AdministradorFormEgresados
    template_name = 'administrador/adminFormEgresado.html'
    success_url = reverse_lazy('administrador:egresado_listar')
    
class EgresadoUpdate(UpdateView):
    model = Egresado
    form_class = AdministradorFormEgresados
    template_name = 'administrador/adminFormEgresado.html'
    success_url = reverse_lazy('administrador:egresado_listar')
    
class EgresadoDelete(DeleteView):
    model = Egresado
    template_name = 'administrador/egresadoEliminar.html'
    success_url = reverse_lazy('administrador:egresado_listar')

