import const
from song import Song


class Album:

    # it gets a data which is a dict of id and name

    def __init__(self, id: str, name: str):
        self.id: str = id
        self.name: str = name
        self._songs_in_album = []

    def add_song_to_album(self, song: Song):
        self._songs_in_album.append(song)
