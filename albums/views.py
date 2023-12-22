from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.

def add_album(request):
    if request.method=='POST':
        album= forms.AlbumForm(request.POST)
        if album.is_valid():
            print(album.cleaned_data)
            album.save()
            return redirect('add_album')
        else:
            print(album.errors)   
    album= forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album})

def edit_album(request, id):
    take_album= models.Album.objects.get(pk=id)
    album= forms.AlbumForm(instance=take_album)
    if request.method=='POST':
        album= forms.AlbumForm(request.POST, instance=take_album)
        if album.is_valid():
            album.save()
            return redirect('home')
        
    return render(request, 'add_album.html', {'form': album})

def delete_album(request, id):
    take_album= models.Album.objects.get(pk=id)
    take_album.delete()
    return redirect('home')