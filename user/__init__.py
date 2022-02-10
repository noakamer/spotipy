import inspect

from playlist import Playlist
from typing import List
import const
from log import debug_log, info_log, warning_log, error_log
from exceptions import CantAddAnotherPlaylistException, ThisPlaylistNameAlreadyExistException, \
    PlaylistNameDoesNotExistException, ArtistDoesNotExistException
from extract import convert_data_to_objects


def get_artist_by_name(artist_name: dict):
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
        elif get_artist_by_name(username):
            self.is_premium = premium
        else:
            self.is_premium = premium
        self.playlists: List[Playlist] = []
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "created the user successfully")

    def add_playlist(self, name: str):
        if not self.is_premium and len(self.playlists) == 5:
            raise CantAddAnotherPlaylistException
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                raise ThisPlaylistNameAlreadyExistException
        self.playlists.append(Playlist(name, self.is_premium))
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "added the playlist successfully")

    def get_playlist(self, name: str):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                call_stack = inspect.stack()
                func_name = call_stack[0][3]
                info_log(__name__, func_name, "find the playlist")
                return playlist
        raise PlaylistNameDoesNotExistException

    def get_all_artists(self):
        counter = 0
        for artist in const.LIST_OF_ARTISTS:
            if (not self.is_premium and counter < 5) or self.is_premium:
                print(artist.name)
                counter += 1
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "printed all the artists successfully")

    def get_artist_album(self, artist_id: str):
        is_exist = False
        for artist in const.LIST_OF_ARTISTS:
            if artist.id == artist_id:
                is_exist = True
                counter = 0
                for album in artist.get_albums():
                    if (not self.is_premium and counter < 5) or self.is_premium:
                        print(album.name)
                        counter += 1
                call_stack = inspect.stack()
                func_name = call_stack[0][3]
                info_log(__name__, func_name, "printed artist albums successfully")
        if not is_exist:
            raise ArtistDoesNotExistException

    def get_top_10_artist_songs(self, artist_id: str):
        all_songs = []
        is_exist = False
        for artist in const.LIST_OF_ARTISTS:
            if artist.id == artist_id:
                is_exist = True
                for album in artist.get_albums():
                    all_songs += album.get_album_songs()
                call_stack = inspect.stack()
                func_name = call_stack[0][3]
                info_log(__name__, func_name, "added all artist songs successfully")
        if not is_exist:
            raise ArtistDoesNotExistException
        sorted_list = sorted(all_songs, key=lambda song: song.popularity, reverse=True)
        counter = 0
        for i in sorted_list:
            if (not self.is_premium and counter < 5) or (self.is_premium and counter < 10):
                counter += 1
                print(i.to_string())
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "printed top artist songs successfully")

    def get_albums_songs(self, album_id: str):
        is_exist = False
        for artist in const.LIST_OF_ARTISTS:
            if artist.album_exist(album_id):
                is_exist = True
                counter = 0
                for song in artist.get_album_by_id(album_id).get_album_songs():
                    if (not self.is_premium and counter < 5) or self.is_premium:
                        counter += 1
                        print(song.to_string())
                call_stack = inspect.stack()
                func_name = call_stack[0][3]
                info_log(__name__, func_name, "printed album songs successfully")
        if not is_exist:
            raise ArtistDoesNotExistException
