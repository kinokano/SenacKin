from django.shortcuts import render
from rest_framework import viewsets
from api.models import Usuarios, Gastos
from api.serializers import UsuariosSerializer, GastosSerializer

# Create your views here.

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer