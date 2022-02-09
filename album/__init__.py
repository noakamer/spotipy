from typing import List
from song import Song


class Album:

    def __init__(self, album_id: str, name: str):
        self.id: str = album_id
        self.name: str = name
        self._songs_in_album: List[Song] = []

    def add_song_to_album(self, song: Song):
        self._songs_in_album.append(song)
