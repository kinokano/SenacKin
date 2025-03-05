from django.shortcuts import render
from api.models import Usuarios, Gastos

def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def gastos(request):
    gastos = Gastos.objects.all()
    return render(request, 'gastos.html', {'gastos': gastos})

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')