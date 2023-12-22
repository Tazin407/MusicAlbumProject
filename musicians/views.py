from django.shortcuts import render,redirect
from .import forms
# Create your views here.

def add_musician(request):
    if request.method=='POST':
        musician=forms.MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()
            print(musician.cleaned_data['first_name'])
            return redirect('add_musician')
            
    musician=forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': musician})
