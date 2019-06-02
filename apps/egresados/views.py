from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from apps.liderAutoevaluacion.models import Evento
from apps.egresados.forms import inscripcionFormEgresados
from apps.liderAutoevaluacion.forms import liderAutoevaluacionFormEvento

# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = 'egresados/registrar.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('liderAutoevaluacion:evento_listar')


def index(request):
    return HttpResponse("Pagina ppal de egresados")

class EventoList(ListView):
    model = Evento
    template_name = 'liderAutoevaluacion/eventoListar.html'

class InscripcionCreate(CreateView):
    model = Evento
    template_name = 'egresados/inscripcionForm.html'
    form_class = liderAutoevaluacionFormEvento
    second_form_class = inscripcionFormEgresados
    success_url = reverse_lazy('liderAutoevaluacion:evento_listar')
    
    def get_context_data(self, **kwargs):
        context = super(InscripcionCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            inscripcion = form.save(commit = False)
            inscripcion.identificacion = form2.save()
            inscripcion.save()
            return HttpResponseRedirect(self.get_succes_url())
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))
        