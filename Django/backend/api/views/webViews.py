from django.shortcuts import render
from api.models import Aluno

def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'home.html', {'alunos': alunos})