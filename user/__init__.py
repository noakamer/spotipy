import inspect
import const
from playlist import Playlist
from typing import List
from log import info_log
from exceptions import CantAddAnotherPlaylistException, ThisPlaylistNameAlreadyExistException, \
    PlaylistNameDoesNotExistException, ArtistDoesNotExistException
from extract_and_transform import load_to_the_relevant_objects


def is_artist_exist(artist_name: dict):
    for artist in const.LIST_OF_ARTISTS:
        if artist_name == artist.name:
            return True
    return False


class User:
    # TODO what if it is an artist?
    def __init__(self, username: str, password: str, premium=None):
        self.username = username
        self.password = password
        if premium is None:
            self.is_premium = False
        elif is_artist_exist(username):
            self.is_premium = True
        else:
            self.is_premium = premium
        self.playlists: List[Playlist] = []
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], "created the user successfully")

    def add_playlist(self, name: str):
        if not self.is_premium and len(self.playlists) == 5:
            raise CantAddAnotherPlaylistException
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                raise ThisPlaylistNameAlreadyExistException
        self.playlists.append(Playlist(name, self.is_premium))
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], "added the playlist successfully")

    def get_playlist(self, name: str):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                call_stack = inspect.stack()
                info_log(__name__, call_stack[0][3], "find the playlist")
                return playlist
        raise PlaylistNameDoesNotExistException

    def get_all_artists(self):
        counter = 0
        for artist in const.LIST_OF_ARTISTS:
            if (not self.is_premium and counter < 5) or self.is_premium:
                print(artist.name)
                counter += 1
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], "printed all the artists successfully")

    def get_artist_album(self, artist_id: str):
        artist = load_to_the_relevant_objects.get_artist(artist_id)
        if artist is None:
            raise ArtistDoesNotExistException
        else:
            counter = 0
            for album in artist.get_albums():
                if (not self.is_premium and counter < 5) or self.is_premium:
                    print(album.name)
                    counter += 1
            call_stack = inspect.stack()
            info_log(__name__, call_stack[0][3], "printed artist albums successfully")

    def get_top_10_artist_songs(self, artist_id: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        artist = load_to_the_relevant_objects.get_artist(artist_id)
        if artist is None:
            raise ArtistDoesNotExistException
        all_songs = []
        for album in artist.get_albums():
            all_songs += album.get_album_songs()
        info_log(__name__, func_name, "added all artist songs successfully")
        sorted_list = sorted(all_songs, key=lambda song: song.popularity, reverse=True)
        counter = 0
        for i in sorted_list:
            if (not self.is_premium and counter < 5) or (self.is_premium and counter < 10):
                counter += 1
                print(i.to_string())
        info_log(__name__, func_name, "printed top artist songs successfully")

    def get_albums_songs(self, album_id: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        is_exist = False
        for artist in const.LIST_OF_ARTISTS:
            if artist.album_exist(album_id):
                is_exist = True
                counter = 0
                for song in artist.get_album_by_id(album_id).get_album_songs():
                    if (not self.is_premium and counter < 5) or self.is_premium:
                        counter += 1
                        print(song.to_string())
                info_log(__name__, func_name, "printed album songs successfully")
        if not is_exist:
            raise ArtistDoesNotExistException
