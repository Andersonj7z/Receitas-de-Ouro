from django.db import models


class Receita(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.TextField(max_length=150)
    ingredients = models.TextField()
    preparo = models.TextField()
    imagem = models.ImageField(upload_to='receitas/', null=True, blank=True)

    def __str__(self):
        return self.titulo
