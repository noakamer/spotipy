import inspect
from song import Song
from typing import List
from exceptions import CantAddAnotherPlaylistException
from log import info_log


class Playlist:
    def __init__(self, name: str, premium):
        self.playlist_name: str = name
        self.playlist: List[Song] = []
        self.is_premium = premium
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], f"created {self.playlist_name} playlist successfully")

    def add_song(self, song: Song):
        if not self.is_premium and len(self.playlist) == 20:
            raise CantAddAnotherPlaylistException
        self.playlist.append(song)
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], "added the song successfully")
