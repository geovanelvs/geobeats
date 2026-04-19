from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Music(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    tempo = models.CharField(max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    # Adicione esta linha abaixo:
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): return self.titulo

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    musicas = models.ManyToManyField(Music, related_name='playlists')

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    ano = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
