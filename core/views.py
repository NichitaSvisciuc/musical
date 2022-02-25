from django.views.generic.list import ListView
from django.views.generic import DetailView, View

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *
from .forms import *

import random

class AlbumView(DetailView):
	model = Album
	template_name = "album_info.html"

class MusicView(DetailView):	
	model = Song
	template_name = "tracks_detail_view.html"

	context_object_name = 'song'

	# def get_context_data(self, **kwargs):

	#     context = super().get_context_data(**kwargs)

	#     context["my_object"] = self.object
	#     return context

def musicList(request):

	search_query = request.GET.get('search', '')

	if request.user.is_authenticated:
		albums = Album.objects.filter(user = request.user)
	else:
		albums = Album.objects.all()

	if search_query:
		songs = Song.objects.filter(Q(song_title__icontains = search_query))
	else:	
		songs = Song.objects.all()

	context = {
		'songs' : songs,
		'albums' : albums,
	}

	return render(request, 'music.html', context)

@login_required
def add_to_playlist(request):
	song_id = request.GET.get('song_id')	
	album_id = request.GET.get('album_id')	

	print(song_id)
	print(album_id)

	curent_album = Album.objects.get(id = album_id)
	curent_song = Song.objects.get(id = song_id)

	curent_album.songs.add(curent_song)
	curent_album.save()

	return redirect('music')

@login_required
def create_playlist(request):

	form = AlbumForm()

	return render(request, 'create.html', {'form' : form})	

@login_required
def create(request):	

	if request.method == "POST":
		form = AlbumForm(request.POST, request.FILES)

		if form.is_valid():

			album = form.save(commit = False)

			album.user = request.user
			album.published = False
			album.slug = album.album_title + str(random.randint(1000, 10000))

			album.save()

		return redirect('albums')

	else:
	   form = AlbumForm()

	return redirect('home')		

@login_required
def delete_album(request):

	id = request.GET.get('album_id')

	album = Album.objects.get(id = id)
	album.delete()	

	return redirect('albums')

def home(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')

@login_required
def tracks(request):

	track_fav = Tracks_fav.objects.get(user = request.user)
	print(track_fav)

	context = {
		'tracks' : track_fav,
	}

	return render(request, 'tracks.html', context)

@login_required
def add_to_fav(request):

	song_id = request.GET.get('song_id')	
	curent_song = Song.objects.get(id = song_id)

	fav_playlist = Tracks_fav.objects.get(user = request.user)

	if curent_song in fav_playlist.songs.all():

		return redirect('music')
	else:

		curent_song.likes += 1
		curent_song.save()

		fav_playlist.songs.add(curent_song)
		fav_playlist.save()

	return redirect('music')

@login_required
def delete_from_fav(request):

	song_id = request.GET.get('song_id')	
	curent_song = Song.objects.get(id = song_id)

	curent_song.likes -= 1
	curent_song.save()

	fav_playlist = Tracks_fav.objects.get(user = request.user)
	fav_playlist.songs.remove(curent_song)
	fav_playlist.save()

	return redirect('tracks')	


def contact(request):
	return render(request, 'contact.html')

@login_required
def remove_from_album(request):

	album_id = request.GET.get('album_id')
	album_slug = request.GET.get('album_slug')
	song_id = request.GET.get('song_id')

	song = Song.objects.get(id = song_id)
	album = Album.objects.get(id = album_id)
	
	album.songs.remove(song)

	return redirect('album', slug = album_slug)

@login_required
def albums(request):

	search_query = request.GET.get('search', '')

	if search_query:
		albums = Album.objects.filter(Q(album_title__icontains = search_query) | Q(genre__icontains = search_query), user = request.user, published = False)
	else:
		albums = Album.objects.filter(user = request.user, published = False)	

	context = {
		'albums' : albums,
	}

	return render(request, 'album.html', context)

def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():

			form.save()	

			return redirect('login')
	else:
		form = UserRegisterForm()
	

	return render(request, 'reg.html', {'form': form})	

@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        Tracks_fav.objects.create(user=instance)	

def add_views(request):
	
	song_id = request.GET.get('song_id')
	curent_song = Song.objects.get(id = song_id)

	if request.user in curent_song.viewers.all():

		return HttpResponse(status = 200)
	else:
		curent_song.viewers.add(request.user)

		curent_song.views += 1
		curent_song.save()

	return HttpResponse(status = 200) 

def add_comment(request):

	song_id = request.GET.get('song_id')
	curent_song = Song.objects.get(id = song_id)

	comment_text = request.GET.get('text')
	comment = Comment.objects.create(user = request.user, text = comment_text)

	curent_song.comments.add(comment)
	curent_song.save()

	return redirect('music_view', slug = curent_song.slug)	