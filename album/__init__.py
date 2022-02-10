import inspect
from typing import List
from song import Song
from log import debug_log, info_log, warning_log, error_log


class Album:

    def __init__(self, album_id: str, name: str):
        self.id: str = album_id
        self.name: str = name
        self._songs_in_album: List[Song] = []
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "created album successfully")

    def add_song_to_album(self, song: Song):
        self._songs_in_album.append(song)
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "created song to album successfully")

    def get_album_songs(self):
        return self._songs_in_album
