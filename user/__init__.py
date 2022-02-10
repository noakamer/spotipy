import inspect
import const
from playlist import Playlist
from typing import List
from log import info_log, error_log
from exceptions import CantAddAnotherPlaylistException, ThisPlaylistNameAlreadyExistException, \
    PlaylistNameDoesNotExistException, ArtistDoesNotExistException
from extract_and_transform import load_to_the_relevant_objects


def get_artist_by_name(artist_name: dict):
    for artist in const.LIST_OF_ARTISTS:
        if artist_name == artist.name:
            return artist
    return None


class User:
    def __init__(self, username: str, password: str, premium=None):
        self.username = username
        self.password = password
        self.is_artist = False
        self.artist = get_artist_by_name(username)
        if self.artist is not None:
            self.is_premium = True
            self.is_artist = True
        elif premium is None:
            self.is_premium = False
        else:
            self.is_premium = premium
        self.playlists: List[Playlist] = []
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], "created the user successfully")

    def add_playlist(self, name: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        try:
            if not self.is_premium and len(self.playlists) == 5:
                raise CantAddAnotherPlaylistException
            for playlist in self.playlists:
                if playlist.playlist_name == name:
                    raise ThisPlaylistNameAlreadyExistException
            self.playlists.append(Playlist(name, self.is_premium))
            info_log(__name__, func_name, "added the playlist successfully")
        except CantAddAnotherPlaylistException:
            error_log(__name__, func_name, CantAddAnotherPlaylistException.__name__)
        except ThisPlaylistNameAlreadyExistException:
            error_log(__name__, func_name, ThisPlaylistNameAlreadyExistException.__name__)

    def get_playlist(self, name: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        try:
            for playlist in self.playlists:
                if playlist.playlist_name == name:
                    info_log(__name__, func_name, "find the playlist")
                    return playlist
            raise PlaylistNameDoesNotExistException
        except PlaylistNameDoesNotExistException:
            error_log(__name__, func_name, PlaylistNameDoesNotExistException.__name__)

    def get_all_artists(self):
        counter = 0
        for artist in const.LIST_OF_ARTISTS:
            if (not self.is_premium and counter < 5) or self.is_premium:
                print(artist.name)
                counter += 1
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], "printed all the artists successfully")

    def get_artist_album(self, artist_id: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        try:
            artist = load_to_the_relevant_objects.get_artist(artist_id)
            if artist is None:
                raise ArtistDoesNotExistException
            else:
                counter = 0
                for album in artist.get_albums():
                    if (not self.is_premium and counter < 5) or self.is_premium:
                        print(album.name)
                        counter += 1
                info_log(__name__, func_name, "printed artist albums successfully")
        except ArtistDoesNotExistException:
            error_log(__name__, func_name, ArtistDoesNotExistException.__name__)

    def get_top_10_artist_songs(self, artist_id: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        try:
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
        except ArtistDoesNotExistException:
            error_log(__name__, func_name, ArtistDoesNotExistException.__name__)

    def get_albums_songs(self, album_id: str):
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        try:
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
        except ArtistDoesNotExistException:
            error_log(__name__, func_name, ArtistDoesNotExistException.__name__)

