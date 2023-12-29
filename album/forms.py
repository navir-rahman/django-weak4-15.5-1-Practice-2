from django import forms
from .models import Album

class AuthorForm(forms.ModelForm):
    class Meta: 
        model = Album
        fields = '__all__'
        labels = { 
            'album_name' : 'album name',
            'musician' : 'name',
            'release_date': 'release date',
        }
        widgets  = { 
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
