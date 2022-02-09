from song import Song
from typing import List


class Playlist:
    def __init__(self, name: str):
        self.playlist_name: str = name
        self.playlist: List[Song] = []

    def add_song(self, song: Song):
        self.playlist.append(song)
