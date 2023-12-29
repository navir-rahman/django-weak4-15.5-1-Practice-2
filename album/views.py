from django.shortcuts import render, redirect
from .forms import AuthorForm
from . import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        post_form = AuthorForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_album')
    else:
        post_form = AuthorForm()
    return render(request, 'all_froms.html', {'form': AuthorForm, "from_name": 'album'})

def edit_album(request, id):
    album = models.Album.objects.get(pk = id)
    album_form = AuthorForm(instance = album)
    if request.method == 'POST':
        album_form = AuthorForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'all_froms.html', {'form': album_form, "from_name": 'album'})
        
 
def delete_album(request, id):
    album =  models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')