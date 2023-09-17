from django.db import models


# Create your models here.
# Definindo Colunas que teremos no banco de dados
class ProjetoDjango(models.Model):
    filme = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.filme
