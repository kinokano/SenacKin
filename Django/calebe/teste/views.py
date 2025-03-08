from rest_framework import viewsets
from .models import AutoresCascade, LivrosCascade, AutoresProtect, LivrosProtect
from .serializers import AutoresCascadeSerializer, AutoresProtectSerializer, LivrosCascadeSerializer, LivrosProtectSerializer

class AutoresCascadeViewSet(viewsets.ModelViewSet):
    queryset = AutoresCascade.objects.all()
    serializer_class =  AutoresCascadeSerializer

class LivrosCascadeViewSet(viewsets.ModelViewSet):
    queryset = LivrosCascade.objects.all()
    serializer_class = LivrosCascadeSerializer

class AutoresProtectViewSet(viewsets.ModelViewSet):
    queryset = AutoresProtect.objects.all()
    serializer_class =  AutoresProtectSerializer

class LivrosProtectViewSet(viewsets.ModelViewSet):
    queryset = LivrosProtect.objects.all()
    serializer_class = LivrosProtectSerializer
