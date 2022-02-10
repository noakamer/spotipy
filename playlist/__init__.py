import inspect

from song import Song
from typing import List
from exceptions import CantAddAnotherPlaylistException
from log import debug_log, info_log, warning_log, error_log


class Playlist:
    def __init__(self, name: str, premium=None):
        self.playlist_name: str = name
        self.playlist: List[Song] = []
        if premium is None:
            self.is_premium = False
        else:
            self.is_premium = premium
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, f"created {self.playlist_name} playlist successfully")

    def add_song(self, song: Song):
        # TODO should add the song by name and not by song object
        if not self.is_premium and len(self.playlist) == 20:
            raise CantAddAnotherPlaylistException
        self.playlist.append(song)
        call_stack = inspect.stack()
        func_name = call_stack[0][3]
        info_log(__name__, func_name, "added the song successfully")
