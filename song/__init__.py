import const


class Song:
    def __init__(self, data: dict):
        # self.album = Album(data.get(const.KEY_OF_SONG).get(const.ALBUM))
        self.popularity = data.get(const.KEY_OF_SONG).get(const.POPULARITY)
        self.id = data.get(const.KEY_OF_SONG).get(const.ID)
        self.name = data.get(const.KEY_OF_SONG).get(const.NAME)
        # self.artist = Artist(data.get(const.KEY_OF_SONG).get(const.ARTISTS))
