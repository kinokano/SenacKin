from rest_framework import serializers

from .models import AutoresCascade, AutoresProtect, LivrosCascade, LivrosProtect

class AutoresCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoresCascade
        fields = '__all__'
    
class LivrosCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivrosCascade
        fields = '__all__'

class AutoresProtectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoresProtect
        fields = '__all__'
    
class LivrosProtectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivrosProtect
        fields = '__all__'
