from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.apiViews import *
from api.views.webViews import *

router = DefaultRouter()
# router.register('funcionarios', FuncionarioViewSet)
# router.register('produtos', ProdutoViewSet)
# router.register('categorias', CategoriaViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home, name="home"),
    path('criarAluno/', criarAluno, name="criarAluno"),
    path('login/', login, name='login'),
    

]