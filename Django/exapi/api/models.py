from django.db import models
# from django import forms
# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField( max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField( max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome

class Gastos(models.Model):
    nome = models.CharField( max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    horario = models.TimeField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
