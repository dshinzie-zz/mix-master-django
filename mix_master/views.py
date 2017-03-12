from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artist, Song, Playlist
from .forms import ArtistForm, SongForm, PlaylistForm

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
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'artists/new.html', {'form': form})

def artist_song_new(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if(request.method) == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.published_date = timezone.now()
            song.artist = artist
            song.save()
            return redirect('artist_list')
    else:
        form = SongForm()
    return render(request, 'artists/songs/new.html', {'form': form, 'artist': artist})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'songs/detail.html', {'song': song})

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/list.html', {'playlists': playlists})

def playlist_detail(request, pk):
    pass

def playlist_new(request):
    songs = Song.objects.all()
    if(request.method) == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            input_songs = request.POST.getlist('songs')
            playlist = form.save(commit=False)
            playlist.published_date = timezone.now()
            playlist.save()
            for song in input_songs:
                playlist.songs.add(song)
            playlist.save()
            return redirect('playlist_list')
    else:
        form = PlaylistForm()
    return render(request, 'playlists/new.html', {'form': form, 'songs': songs})
