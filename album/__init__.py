import const


class album():

    # it gets a data which is a dict of id and name

    def __init__(self, data):
        self.id = data.get(const.ID)
        self.name = data.get(const.NAME)
        self.songs_in_album = [{}]

    def add_song_to_album(self, song):
        self.songs_in_album.append({const.ID: song.id, const.NAME: song.name})
