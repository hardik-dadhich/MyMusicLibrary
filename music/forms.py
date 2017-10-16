from django.contrib.auth.models import User
from django import forms
from .models import Album, Song


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
