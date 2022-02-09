import const
from album import Album
from song import Song


class Artist:
    def __init__(self, data):
        self.id: str = data[0].get(const.ID)
        self.name: str = data[0].get(const.NAME)
        self._albums: Album = []
        self._singles: Song = []

    def album_exist(self):
        pass

    def add_album(self, album: Album):
        self._albums.append(album)

    def add_single(self, single: Song):
        self._singles.append(single)

    def get_albums(self):
        return self._albums

    def get_singles(self):
        return self._singles
