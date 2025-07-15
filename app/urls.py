from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('pacientes/', views.pacientes, name='pacientes'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('triagem/', views.triagem, name='triagem'),
    path('exames/', views.exames, name='exames'),
    path('notificacoes/', views.notificacoes, name='notificacoes'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
