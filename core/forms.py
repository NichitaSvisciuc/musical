from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm 

from django import forms
from .models import *
  
class AlbumForm(forms.ModelForm):
  
	class Meta:
		model = Album

		widgets = {
            'album_title': forms.TextInput(attrs={'class': 'contactus', 'placeholder' : 'Album title'}),
            'genre': forms.TextInput(attrs={'class': 'contactus', 'placeholder' : 'Genre'}),
        }

		fields = ['album_title', 'genre', 'album_logo']


class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User

		widgets = {
			'username' : forms.TextInput(attrs={'class': 'input-group'}),
			'password1' : forms.TextInput(attrs={'class': 'input-group'}),
			'password2' : forms.TextInput(attrs={'class': 'input-group'}),
		}

		fields = ['username', 'password1', 'password2'] 

class UploadSongForm(forms.ModelForm):

	class Meta:
		model = Song

		widgets = {
			'song_title' : forms.TextInput(attrs={'class': 'input-group', 'placeholder' : 'Song title'}),
			'song_artist' : forms.TextInput(attrs={'class': 'input-group', 'placeholder' : 'Artist name'}),
		}

		fields = ['song_title', 'song_artist', 'image', 'file'] 		