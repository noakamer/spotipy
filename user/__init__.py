from playlist import Playlist
from typing import List


class User:
    def __init__(self, username: str, password: str, premium=None):
        self.username = username
        self.password = password
        if premium is None:
            self.is_premium = False
        else:
            self.is_premium = premium
        self.playlists: List[Playlist] = []

    def add_playlist(self, name: str):
        if not self.is_premium and len(self.playlists) == 5:
            # throw exception "you cant add another playlist"
            pass
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                # should throw exception "already have this playlist name"
                pass
        self.playlists.append(Playlist(name))

    def get_playlist(self, name: str):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                return playlist
        # should throw exception "playlist_not_exist"
