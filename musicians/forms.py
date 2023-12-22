from django import forms 
from .import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model= models.Musician
        fields= '__all__'
        labels= {
            'first_name':'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Mobile Number',
            'instrument': 'Played Instrument',
        }
    