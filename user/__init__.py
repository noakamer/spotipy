from playlist import Playlist
from typing import List


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.playlists: List[Playlist] = []

    def add_playlist(self, name: str):
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
