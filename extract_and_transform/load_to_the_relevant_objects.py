import inspect
from artist import Artist
from song import Song
from album import Album
import const
from log import info_log


def get_artist(artist_data: dict):
    call_stack = inspect.stack()
    func_name = call_stack[0][3]
    for artist in const.LIST_OF_ARTISTS:
        if artist_data.get(const.ID) == artist.id:
            info_log(__name__, func_name, "returned new artist successfully")
            return artist
    info_log(__name__, func_name, "artist not found")
    return None


def create_new_artist(data: dict, artist_data: dict, song: Song):
    artist = Artist(artist_data.get(const.ID), artist_data.get(const.NAME))
    album = Album(data.get(const.ALBUM).get(const.ID), data.get(const.ALBUM).get(const.NAME))
    artist.add_album(album)
    artist.get_album_by_id(album.id).add_song_to_album(song)
    call_stack = inspect.stack()
    info_log(__name__, call_stack[0][3], "returned new artist successfully")
    return artist


def convert_data_to_object(list_of_all_data: list):
    call_stack = inspect.stack()
    for data in list_of_all_data:
        data = data.get(const.KEY_OF_SONG)
        song = Song(data.get(const.POPULARITY), data.get(const.ID), data.get(const.NAME))
        for artist_data in data.get(const.ARTISTS):
            artist = get_artist(artist_data)
            if artist is not None:
                if artist.album_exist(data.get(const.ALBUM).get(const.NAME)):
                    artist.get_album_by_name(data.get(const.ALBUM).get(const.NAME)).add_song_to_album(song)
                else:
                    album = Album(data.get(const.ALBUM).get(const.ID), data.get(const.ALBUM).get(const.NAME))
                    album.add_song_to_album(song)
                    artist.add_album(album)
            else:
                artist = create_new_artist(data, artist_data, song)
                const.LIST_OF_ARTISTS.append(artist)
    info_log(__name__, call_stack[0][3], "function ended successfully")
