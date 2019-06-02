from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from apps.liderAutoevaluacion.models import Evento
from apps.liderAutoevaluacion.forms import liderAutoevaluacionFormEvento
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'liderAutoevaluacion/index.html')

def liderAutoevaluacion_viewEvento(request):
    if request.method == 'POST':
        form = liderAutoevaluacionFormEvento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liderAutoevaluacion:index')
    else:
        form = liderAutoevaluacionFormEvento()
    return render(request, 'liderAutoevaluacion/liderForm.html', {'form': form})

class EventoList(ListView):
    model = Evento
    template_name = 'liderAutoevaluacion/eventoListar.html'

class EventoCreate(ListView):
    model = Evento
    form_class = liderAutoevaluacionFormEvento
    template_name = 'liderAutoevaluacion/liderForm.html'
    success_url = reverse_lazy('liderAutoevaluacion:evento_listar')


class EventoUpdate(UpdateView):
    model = Evento
    form_class = liderAutoevaluacionFormEvento
    template_name = 'liderAutoevaluacion/liderForm.html'
    success_url = reverse_lazy('liderAutoevaluacion:evento_listar')


class EventoDelete(DeleteView):
    model = Evento
    template_name = 'liderAutoevaluacion/eventoEliminar.html'
    success_url = reverse_lazy('liderAutoevaluacion:evento_listar')
