from artist import Artist
from song import Song
from album import Album
import const


def get_artist(artist_data: dict):
    for artist in const.LIST_OF_ARTISTS:
        if artist_data.get(const.ID) == artist.id:
            return artist
    return None


def create_new_artist(data: dict, artist_data: dict, song: Song):
    artist = Artist(artist_data.get(const.ID), artist_data.get(const.NAME))
    album = Album(data.get(const.ALBUM).get(const.ID), data.get(const.ALBUM).get(const.NAME))
    artist.add_album(album)
    artist.get_album_by_name(album.name).add_song_to_album(song)
    return artist


def convert_data_to_object(list_of_all_data: list):
    for data in list_of_all_data:
        data = data.get(const.KEY_OF_SONG)
        song = Song(data)
        for artist_data in data.get(const.ARTISTS):
            artist = get_artist(artist_data)
            if artist is not None:
                if artist.album_exist(data.get(const.ALBUM).get(const.NAME)):
                    a = artist.get_album_by_name(data.get(const.ALBUM).get(const.NAME))
                    a.add_song_to_album(song)
                else:
                    album = Album(data.get(const.ALBUM).get(const.ID), data.get(const.ALBUM).get(const.NAME))
                    album.add_song_to_album(song)
                    artist.add_album(album)
            else:
                artist = create_new_artist(data, artist_data, song)
                const.LIST_OF_ARTISTS.append(artist)
