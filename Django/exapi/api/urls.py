from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.apiViews import UsuariosViewSet, GastosViewSet
from api.views.webViews import usuarios, gastos, index, cadastrar

router = DefaultRouter()
# router.register('funcionarios', FuncionarioViewSet)
# router.register('produtos', ProdutoViewSet)
# router.register('categorias', CategoriaViewSet)
router.register('usuarios', UsuariosViewSet)
router.register('gastos', GastosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('usuarios/', usuarios, name='usuarios'),
    path('gastos/', gastos, name='gastos'),
    path('', index, name='index'),
    path('cadastrar/', cadastrar, name='cadastrar')

]