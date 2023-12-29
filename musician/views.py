from django.shortcuts import render, redirect
from .forms import MusicianFrom
from .models import Musician
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        post_form = MusicianFrom(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_musician')
    else:
        post_form = MusicianFrom()
    return render(request, 'all_froms.html', {'form': MusicianFrom, "from_name": "musician"}) 

def edit_musician(request,id):
    musician = Musician.objects.get(pk=id)
    musician_form = MusicianFrom(instance  = musician)
    if request.method == 'POST':
        musician_form = MusicianFrom(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    return render(request, 'all_froms.html', {'form': musician_form, "from_name": "musician"}) 
    
