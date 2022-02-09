from artist import Artist
from song import Song
from album import Album
import const

def get_artist(artist_data: dict):
    for artist in const.LIST_OF_ARTISTS:
        if artist_data.get(const.ID) == artist.get(const.ID):
            return artist
    return None


def convert_data_to_object(list_of_all_data: list):
    for data in list_of_all_data:
        song = Song(data)
        for artist_data in data.get(const.ARTISTS):
            artist = get_artist(artist_data)
            if artist is not None:
                if artist.album_exist(data.get(const.ALBUM).get(const.NAME)):
                    artist.get_album_by_name(data.get(const.ALBUM).get(const.NAME)).add_song_to_album(song)
                else:
                    album = Album(data.get(const.ALBUM))
                    album.add_song_to_album(song)
                    artist.add_album(album)
            else:
                artist = Artist(artist_data)
                album = Album(data.get(const.ALBUM))
                artist.add_album(album)
                artist.get_album_by_name(album.name).add_song_to_album(song)
                const.LIST_OF_ARTISTS.append(artist)
