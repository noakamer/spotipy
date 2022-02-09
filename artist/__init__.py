import const
from album import Album
from song import Song


class Artist:
    def __init__(self, id: str, name: str):
        self.id: str = id
        self.name: str = name
        self._albums: list[Album] = []
        self._singles: Song = []

    def get_album_by_name(self, album_name: str):
        for album in self._albums:
            if album.name == album_name:
                return album
        return None

    def album_exist(self, album_name: str):
        if self.get_album_by_name(album_name) is not None:
            return True
        return False

    def add_album(self, album: Album):
        self._albums.append(album)

    def add_single(self, single: Song):
        self._singles.append(single)

    def get_albums(self):
        return self._albums

    def get_singles(self):
        return self._singles
