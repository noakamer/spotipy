import const


def get_all_artists():
    for artist in const.LIST_OF_ARTISTS:
        print(artist.name)


def get_artist_album(artist_id: str):
    is_exist = False
    for artist in const.LIST_OF_ARTISTS:
        if artist.id == artist_id:
            is_exist = True
            for album in artist.get_albums():
                print(album.name)
    if not is_exist:
        # throw exception
        pass


def get_top_10_artist_songs(artist_id: str):
    all_songs = []
    is_exist = False
    for artist in const.LIST_OF_ARTISTS:
        if artist.id == artist_id:
            is_exist = True
            for album in artist.get_albums():
                all_songs += album.get_album_songs()
    if not is_exist:
        # throw exception
        pass
    sorted_list = sorted(all_songs, key=lambda song: song.population, reverse=True)
    for i in range(10):
        print(sorted_list[i])


def get_albums_songs(album_id: str):
    is_exist = False
    for artist in const.LIST_OF_ARTISTS:
        if artist.album_exist(album_id):
            is_exist = True
            for song in artist.get_album_by_id(album_id).get_album_songs():
                print(song)
    if not is_exist:
        # throw exception
        pass
