from django.urls import path
from .views import (
    HomeView,
    PacienteListView,
    AgendamentoListView,
    TriagemListView,
    ExameListView,
    NotificacaoListView,
    RelatoriosView,
)

urlpatterns = [
    path('', HomeView.as_view(),          name='home'),
    path('pacientes/', PacienteListView.as_view(),   name='pacientes'),
    path('agendamentos/', AgendamentoListView.as_view(), name='agendamentos'),
    path('triagem/', TriagemListView.as_view(),      name='triagem'),
    path('exames/', ExameListView.as_view(),         name='exames'),
    path('notificacoes/', NotificacaoListView.as_view(), name='notificacoes'),
    path('relatorios/', RelatoriosView.as_view(),    name='relatorios'),
]
