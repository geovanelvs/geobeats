from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets

from .models import Music, Playlist
from .forms import MusicForm, PlaylistForm
from .serializers import MusicSerializer, PlaylistSerializer

# ==========================================
# 1. API ViewSets (Para o JSON e Integrações)
# ==========================================
class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    def get_queryset(self):
        # A API também filtra por utilizador logado
        return Music.objects.filter(usuario=self.request.user)

class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    def get_queryset(self):
        return Playlist.objects.filter(usuario=self.request.user)


# ==========================================
# 2. PÁGINA DE REGISTO DE UTILIZADORES
# ==========================================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Agora já pode entrar.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'music/register.html', {'form': form})


# ==========================================
# 3. CRUD DE MÚSICAS (Sistema Web)
# ==========================================
@login_required
def music_list(request):
    # Lista apenas as músicas do utilizador logado
    musicas = Music.objects.filter(usuario=request.user) 
    return render(request, 'music/music_list.html', {'musicas': musicas})

@login_required
def music_add(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.usuario = request.user # Associa o dono automaticamente
            musica.save()
            messages.success(request, "Música adicionada com sucesso!")
            return redirect('music_list')
    else:
        form = MusicForm()
    return render(request, 'music/music_form.html', {'form': form, 'titulo': 'Adicionar Música'})

@login_required
def music_update(request, pk):
    musica = get_object_or_404(Music, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = MusicForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            messages.warning(request, "Música atualizada!")
            return redirect('music_list')
    else:
        form = MusicForm(instance=musica)
    return render(request, 'music/music_form.html', {'form': form, 'titulo': 'Editar Música'})

@login_required
def music_delete(request, pk):
    musica = get_object_or_404(Music, pk=pk, usuario=request.user)
    if request.method == "POST":
        musica.delete()
        messages.error(request, "Música removida!")
        return redirect('music_list')
    return render(request, 'music/music_confirm_delete.html', {'musica': musica})


# ==========================================
# 4. CRUD DE PLAYLISTS (Sistema Web)
# ==========================================
@login_required
def playlist_list(request):
    # Lista apenas as playlists do utilizador logado
    playlists = Playlist.objects.filter(usuario=request.user)
    return render(request, 'music/playlist_list.html', {'playlists': playlists})

@login_required
def playlist_add(request):
    if request.method == 'POST':
        # AQUI: Passamos o user=request.user
        form = PlaylistForm(request.POST, user=request.user)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.usuario = request.user # Associa o dono automaticamente
            playlist.save()
            form.save_m2m() # Salva as relações com as músicas escolhidas
            messages.success(request, "Playlist criada com sucesso!")
            return redirect('playlist_list') 
    else:
        # AQUI: Passamos o user=request.user
        form = PlaylistForm(user=request.user)
    return render(request, 'music/playlist_form.html', {'form': form, 'titulo': 'Criar Nova Playlist'})

@login_required
def playlist_edit(request, id):
    # Garante que só edita se for o dono da playlist
    playlist = get_object_or_404(Playlist, id=id, usuario=request.user) 
    
    if request.method == 'POST':
        # AQUI: Passamos o user=request.user junto com a instance
        form = PlaylistForm(request.POST, instance=playlist, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Playlist atualizada com sucesso!")
            return redirect('playlist_list')
    else:
        # AQUI: Passamos o user=request.user junto com a instance
        form = PlaylistForm(instance=playlist, user=request.user)
        
    return render(request, 'music/playlist_form.html', {'form': form, 'titulo': 'Editar Playlist'})

@login_required
def playlist_delete(request, id):
    # Garante que só apaga se for o dono
    playlist = get_object_or_404(Playlist, id=id, usuario=request.user)
    
    if request.method == 'POST':
        playlist.delete()
        messages.error(request, "Playlist removida!")
        return redirect('playlist_list')
        
    return render(request, 'music/playlist_confirm_delete.html', {'playlist': playlist})