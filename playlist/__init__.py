from song import Song
from typing import List


class Playlist:
    def __init__(self, name: str, premium=None):
        self.playlist_name: str = name
        self.playlist: List[Song] = []
        if premium is None:
            self.is_premium = False
        else:
            self.is_premium = premium

    def add_song(self, song: Song):
        if not self.is_premium and len(self.playlist) == 20:
            # throw exception "you cant add another playlist"
            pass
        self.playlist.append(song)
