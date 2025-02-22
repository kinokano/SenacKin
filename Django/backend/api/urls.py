from django.urls import path
from .views import (listarFuncionarios, cadastrarFuncionario, obterFuncionario)

urlpatterns = [
    path('funcionarios/', listarFuncionarios, name='listarFuncionarios'),
    path('funcionarios/cadastrar', cadastrarFuncionario, name='cadastrarFuncionario'),
    path('funcionarios/<int:id>', obterFuncionario, name='obterFuncionario'),

]