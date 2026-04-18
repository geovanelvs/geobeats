from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Music(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    tempo = models.CharField(max_length=10, help_text="Ex: 3:45")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    musicas = models.ManyToManyField(Music)
    
    def __str__(self):
        return self.nome