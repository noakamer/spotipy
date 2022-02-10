import inspect
from typing import List
from album import Album
from song import Song
from log import debug_log, info_log, warning_log, error_log


class Artist:
    def __init__(self, id: str, name: str):
        self.id: str = id
        self.name: str = name
        self._albums: List[Album] = []
        self._singles: List[Song] = []
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, f"created {self.name} artist successfully")

    def get_album_by_id(self, album_id: str):
        for album in self._albums:
            if album.id == album_id:
                call_stack = inspect.stack()
                func_name = call_stack[0][3]
                info_log(__name__, func_name, "return the album successfully")
                return album
        return None

    def album_exist(self, album_id: str):
        if self.get_album_by_id(album_id) is not None:
            return True
        return False

    def add_album(self, album: Album):
        self._albums.append(album)
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "added the album successfully")

    def add_single(self, single: Song):
        self._singles.append(single)

    def get_albums(self):
        return self._albums

    def get_singles(self):
        return self._singles
