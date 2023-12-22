from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.EmailField()
    phone= models.CharField(max_length=11)
    instrument= models.CharField(max_length=60)
    
    def __str__(self):
        return self.first_name
