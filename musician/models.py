from django.db import models

# Create your models here.
ins_choices = ['band', 'band2']
class Musician(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Instrument = models.Choices(choices = ins_choices)
    
    def __str__(self):
        return self.name