from django.shortcuts import render
from api.models import Usuarios, Gastos

def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def gastos(request):
    gastos = Gastos.objects.all()
    return render(request, 'gastos.html', {'gastos': gastos})