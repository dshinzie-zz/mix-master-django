from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^artists/$', views.artist_list, name='artist_list'),
    url(r'^artists/(?P<pk>\d+)/$', views.artist_detail, name='artist_detail'),
    url(r'^artists/new/$', views.artist_new, name='artist_new'),
    # url(r'^artists/(?P<pk>\d+)/edit/$', views.artist_edit, name='artist_edit'),

    # songs
    url(r'^artists/(?P<pk>\d+)/songs/new/$', views.artist_song_new, name='artist_song_new'),
]
