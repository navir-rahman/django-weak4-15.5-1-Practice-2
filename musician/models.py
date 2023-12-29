from django.db import models

# Create your models here.
#     album_name = models.CharField(max_length=20)
#     # One-to-Many Relationships with musician model
#     musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     release_date = models.DateField()
#     Rating 
class Musician(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Instrument = models.CharField(max_length=20)

    def __str__(self):
        return self.First_Name