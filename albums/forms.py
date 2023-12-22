from django import forms 
from .import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model= models.Album
        fields= "__all__"
        labels={
            'name':'Title',
            'author': 'Author',
            'release_date': 'Release Date',
        }
        widgets={
            'rating': forms.Select(),
        }