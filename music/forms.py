from django import forms
from .models import Music, Playlist, Album

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['titulo', 'artista', 'tempo', 'categoria']

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nome', 'musicas']
        widgets = {
            'musicas': forms.CheckboxSelectMultiple(),
        } 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super(PlaylistForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['musicas'].queryset = Music.objects.filter(usuario=user)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'artista', 'ano']