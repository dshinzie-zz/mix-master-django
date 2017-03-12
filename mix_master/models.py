from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
