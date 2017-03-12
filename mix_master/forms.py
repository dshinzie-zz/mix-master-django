from django import forms
from .models import Artist, Song, Playlist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'image_path',)

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title',)

class PlaylistForm(forms.ModelForm):
    #songs will come into params as request.POST['songs']
    songs = forms.ModelMultipleChoiceField(
        queryset = Song.objects.all(),
        widget  = forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Playlist
        fields = ('name',)
