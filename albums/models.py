from django.db import models
from musicians.models import Musician
import datetime

# Create your models here.
class Album(models.Model):
    
    name= models.CharField(max_length=100)
    author= models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date= models.DateField(default=datetime.datetime.now)
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    
    def __str__(self):
        return self.name
    
    # Album Name
    # One-to-Many Relationships with musician model
    # Album release date
    # Rating between 1-5
