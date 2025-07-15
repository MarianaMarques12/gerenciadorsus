from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def agendamentos(request):
    return render(request, 'agendamentos.html')

def triagem(request):
    return render(request, 'triagem.html')

def exames(request):
    return render(request, 'exames.html')

def notificacoes(request):
    return render(request, 'notificacoes.html')

def relatorios(request):
    return render(request, 'relatorios.html')
