from django.db import models

# Create your models here.
class AutoresCascade(models.Model):
    nome = models.CharField( max_length=255, null=False, blank=False)
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nome

class LivrosCascade(models.Model):
    titulo = models.CharField( max_length=255, null=False, blank=False)
    anoPublicacao = models.DateField()
    idAutor = models.ForeignKey(AutoresCascade, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class AutoresProtect(models.Model):
    nome = models.CharField( max_length=255, null=False, blank=False)
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nome

class LivrosProtect(models.Model):
    titulo = models.CharField( max_length=255, null=False, blank=False)
    anoPublicacao = models.DateField()
    idAutor = models.ForeignKey(AutoresProtect, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


