from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.apiViews import AlunoViewSet
from api.views.webViews import home

router = DefaultRouter()
# router.register('funcionarios', FuncionarioViewSet)
# router.register('produtos', ProdutoViewSet)
# router.register('categorias', CategoriaViewSet)
router.register('alunos', AlunoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home, name="home")

    # path('funcionarios/', listarFuncionarios, name='listarFuncionarios'),
    # path('funcionarios/cadastrar', cadastrarFuncionario, name='cadastrarFuncionario'),
    # path('funcionarios/<int:id>', obterFuncionario, name='obterFuncionario'),

]