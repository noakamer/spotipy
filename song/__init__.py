class Song:
    def __init__(self, data: dict):
        import const
        self.popularity = data.get(const.POPULARITY)
        self.id = data.get(const.ID)
        self.name = data.get(const.NAME)
