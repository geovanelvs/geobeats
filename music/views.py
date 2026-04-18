from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets  # Importação adicionada para a API
from .models import Music
from .forms import MusicForm
from .serializers import MusicSerializer  # Importação adicionada para a API
from django.contrib.auth.forms import UserCreationForm
# VIEWS TRADICIONAIS (INTERFACE WEB / CRUD)
@login_required
def music_list(request):
    # Filtra as músicas: apenas as que pertencem ao usuário logado
    musicas = Music.objects.filter(usuario=request.user) 
    return render(request, 'music/music_list.html', {'musicas': musicas})

@login_required
def music_add(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False) # Cria o objeto mas não salva no banco ainda
            musica.usuario = request.user    # Atribui o utilizador logado automaticamente
            musica.save()                    # Agora sim, salva com o dono
            messages.success(request, "Música adicionada com sucesso!")
            return redirect('music_list')
    # ... resto da função
    else:
        form = MusicForm()
    return render(request, 'music/music_form.html', {'form': form, 'titulo': 'Adicionar Música'})

@login_required
def music_update(request, pk):
    musica = get_object_or_404(Music, pk=pk)
    
    if request.method == "POST":
        form = MusicForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            messages.warning(request, "Música atualizada com sucesso!")
            return redirect('music_list')
    else:
        form = MusicForm(instance=musica)
    return render(request, 'music/music_form.html', {'form': form, 'titulo': 'Editar Música'})

@login_required
def music_delete(request, pk):
    musica = get_object_or_404(Music, pk=pk)
    
    if request.method == "POST":
        musica.delete()
        messages.error(request, "Música removida!")
        return redirect('music_list')
        
    return render(request, 'music/music_confirm_delete.html', {'musica': musica})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Agora você pode entrar.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'music/register.html', {'form': form})

# VIEWS DA API REST (JSON)
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer