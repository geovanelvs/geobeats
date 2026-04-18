from django.contrib import admin
from .models import Categoria, Music, Playlist

# REMOVEMOS as linhas admin.site.register daqui, pois elas causam o erro de duplicidade.

# Configuração para a Categoria aparecer no Admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# Configuração para a Música aparecer no Admin
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'tempo', 'categoria')
    list_filter = ('categoria', 'artista')
    search_fields = ('titulo', 'artista')

# Configuração para a Playlist aparecer no Admin
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario') # Adicionei 'usuario' para você ver quem é o dono
    filter_horizontal = ('musicas',)