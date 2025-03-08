from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoresProtectViewSet, AutoresCascadeViewSet, LivrosCascadeViewSet, LivrosProtectViewSet


router = DefaultRouter()
router.register('autoresCascade', AutoresCascadeViewSet)
router.register('livrosCascade', LivrosCascadeViewSet)
router.register('autoresProtect', AutoresProtectViewSet)
router.register('livrosProtect', LivrosProtectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]