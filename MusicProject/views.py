from django.shortcuts import render
from albums.forms import AlbumForm
from albums.models import Album

def home(request):
    album= Album.objects.all()
    return render(request, 'home.html', {'album':album})


    
    