from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['titulo', 'artista', 'tempo', 'categoria']
        
    def __init__(self, *args, **kwargs):
        """
        Este método inicializa o formulário e aplica a classe 'form-control' 
        do Bootstrap em todos os campos automaticamente.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'