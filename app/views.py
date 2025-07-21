# gerenciadorsus/app/views_and_urls.py

from django.urls import path
from django.views.generic import TemplateView, ListView
from .models import Paciente, Agendamento, Triagem, AgendamentoExame, Notificacao

# --- VIEWS ---

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

class PacienteListView(ListView):
    model = Paciente
    template_name = 'pacientes.html'
    context_object_name = 'pacientes'
    queryset = Paciente.objects.select_related('cidade', 'grupo_risco').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'agendamentos.html'
    context_object_name = 'agendamentos'
    queryset = Agendamento.objects.select_related('paciente', 'medico').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

class TriagemListView(ListView):
    model = Triagem
    template_name = 'triagem.html'
    context_object_name = 'triagens'
    queryset = Triagem.objects.select_related('paciente').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

class ExameListView(ListView):
    model = AgendamentoExame
    template_name = 'exames.html'
    context_object_name = 'exames'
    queryset = AgendamentoExame.objects.select_related('paciente', 'exame_procedimento').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

class NotificacaoListView(ListView):
    model = Notificacao
    template_name = 'notificacoes.html'
    context_object_name = 'notificacoes'
    queryset = Notificacao.objects.select_related('paciente').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

class RelatoriosView(TemplateView):
    template_name = 'relatorios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

# --- URLS ---
