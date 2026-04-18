from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Music
from .forms import MusicForm

@login_required
def music_list(request):
    musicas = Music.objects.all()
    return render(request, 'music/music_list.html', {'musicas': musicas})

@login_required
def music_add(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Música adicionada com sucesso!")
            return redirect('music_list')
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