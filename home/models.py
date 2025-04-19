from django.db import models

class Receita(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=150)
    ingredients = models.TextField()
    preparo = models.TextField()
    imagem = models.ImageField(upload_to='receitas/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True, help_text="Insira a URL do vídeo de preparo (YouTube, etc.)")

    def __str__(self):
        return self.titulo