from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artist
from .forms import ArtistForm

from django.shortcuts import render

def index(request):
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', {'artists': artists})
