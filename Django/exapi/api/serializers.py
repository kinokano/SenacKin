from rest_framework import serializers

from .models import Usuarios, Gastos

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
    
class GastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = '__all__'
    
    