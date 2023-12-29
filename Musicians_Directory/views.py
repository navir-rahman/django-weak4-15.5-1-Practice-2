from django.shortcuts import render
from album.models import Album
from musician.models import Musician
# Create your views here.

def home(request):
    return render(request, 'home.html', {"album" : Album.objects.all() , "musician": Musician.objects.all()})