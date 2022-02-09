import const


class artist():
    def __init__(self, data):
        self.id = data[0].get(const.ID)
        self.name = data[0].get(const.NAME)
        self.albums = []
        self.singles = []

    def add_album(self, album):
        self.albums.append(album)

    def add_single(self, single):
        self.singles.append(single)
