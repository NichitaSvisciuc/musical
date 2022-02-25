from django.urls import path

from .views import *

urlpatterns = [
	path('', home, name = 'home'),
	path('about/', about, name = 'about'),
	path('music/', musicList, name = 'music'),
	path('music_view/<slug>', MusicView.as_view(), name = 'music_view'),
	path('create_playlist/', create_playlist, name = 'create_playlist'),
	path('create/', create, name = 'create'),
	path('delete_album/', delete_album, name = 'delete_album'),
	path('albums/', albums, name = 'albums'),
	path('albums/<slug>/', AlbumView.as_view(), name = 'album'),
	path('remove_from_album/', remove_from_album, name = 'remove_from_album'),
	path('add_to_playlist/', add_to_playlist, name = 'add_to_playlist'),
	path('add_to_fav/', add_to_fav, name = 'add_to_fav'),
	path('delete_from_fav/', delete_from_fav, name = 'delete_from_fav'),
	path('add_comment/', add_comment, name = 'add_comment'),
	path('add_views/', add_views, name = 'add_views'),
	path('tracks/', tracks, name = 'tracks'),
	path('upload_song/', upload_song, name = 'upload_song'),
	path('contact/', contact, name = 'contact'),
]