import inspect
from log import info_log


class Song:
    def __init__(self, popularity, song_id, name):
        self.popularity = popularity
        self.id = song_id
        self.name = name
        call_stack = inspect.stack()
        info_log(__name__, call_stack[0][3], f"created {self.name} song successfully")

    def to_string(self):
        return f"name: {self.name}"
