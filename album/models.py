from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=20)
    # One-to-Many Relationships with musician model
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    Rating = models.IntegerChoices(choices=[0, 1, 2, 3, 4, 5])

    def __str__(self):
        return self.name