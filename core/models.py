from django.contrib.auth.models import User

from django.db import models
import PIL

from django.shortcuts import redirect
from django.shortcuts import reverse

class Song(models.Model):
	
	file = models.FileField(upload_to = 'media/tracks')
	song_title = models.CharField(max_length = 250)
	song_artist = models.CharField(max_length = 250)
	is_favorite = models.BooleanField(default = False)
	likes = models.IntegerField(default = 0)
	viewers = models.ManyToManyField(User)
	views = models.IntegerField(default = 0)
	image = models.ImageField(upload_to = 'media', default = 'media/default.png', null = True, blank = True)
	slug = models.SlugField()

	comments = models.ManyToManyField('Comment')

	def get_absolute_url(self):
		return reverse("music_view", kwargs = {
			'slug' : self.slug
		})	 	

	def __str__(self):
		return self.song_title

class Comment(models.Model):
	
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
	text = models.TextField() 		

class Album(models.Model):
	
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
	album_title = models.CharField(max_length = 300)
	genre = models.CharField(max_length = 100)
	album_logo = models.ImageField(upload_to = 'media', default = 'media/default.png', null = True, blank = True)
	songs = models.ManyToManyField(Song)
	published = models.BooleanField(default = False)
	slug = models.SlugField()

	def get_absolute_url(self):
		return reverse("album", kwargs = {
			'slug' : self.slug
		})	 		

	def __str__(self):
		return self.album_title

class Tracks_fav(models.Model):
	
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
	songs = models.ManyToManyField(Song)	

	def __str__(self):
		return 'Favourite'	