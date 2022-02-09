from song import Song


class Playlist:
    def __init__(self, name: str):
        self.playlist_name = name
        self.playlist: list[Song] = []

    def add_song(self, song: Song):
        self.playlist.append(song)
