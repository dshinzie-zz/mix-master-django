from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    #artists
    url(r'^artists/$', views.artist_list, name='artist_list'),
    url(r'^artists/(?P<pk>\d+)/$', views.artist_detail, name='artist_detail'),
    url(r'^artists/new/$', views.artist_new, name='artist_new'),
    # url(r'^artists/(?P<pk>\d+)/edit/$', views.artist_edit, name='artist_edit'),

    # artist songs
    url(r'^artists/(?P<pk>\d+)/songs/new/$', views.artist_song_new, name='artist_song_new'),

    #songs
    url(r'^songs/$', views.song_list, name='song_list'),
    url(r'^songs/(?P<pk>\d+)/$', views.song_detail, name='song_detail'),

    #playlists
    url(r'^playlists/$', views.playlist_list, name='playlist_list'),
    url(r'^playlists/new/$', views.playlist_new, name='playlist_new'),
    url(r'^playlists/(?P<pk>\d+)/$', views.playlist_detail, name='playlist_detail'),
]
