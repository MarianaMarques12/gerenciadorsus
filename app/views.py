from django.shortcuts import render
from .models import *

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})
