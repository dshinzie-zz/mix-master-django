from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artist
from .forms import ArtistForm

from django.shortcuts import render

def artist_index(request):
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', {'artists': artists})

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
