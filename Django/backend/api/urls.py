from django.urls import path, include
# from .views import (listarFuncionarios, cadastrarFuncionario, obterFuncionario)
from rest_framework.routers import DefaultRouter
from api.views import FuncionarioViewSet

router = DefaultRouter()
router.register('funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls))

    # path('funcionarios/', listarFuncionarios, name='listarFuncionarios'),
    # path('funcionarios/cadastrar', cadastrarFuncionario, name='cadastrarFuncionario'),
    # path('funcionarios/<int:id>', obterFuncionario, name='obterFuncionario'),


]