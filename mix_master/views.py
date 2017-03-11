from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artist, Song
from .forms import ArtistForm, SongForm

from django.shortcuts import render

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists/list.html', {'artists': artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artists/detail.html', {'artist': artist})

def artist_new(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.published_date = timezone.now()
            artist.save()
            return redirect('artist_index')
    else:
        form = ArtistForm()
    return render(request, 'artists/new.html', {'form': form})

def artist_song_new(request, pk):
    if(request.method) == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.published_date = timezone.now()
            song.save()
            return redirect('artist_index')
    else:
        form = SongForm()
    return render(request, 'artists/songs/new.html')
