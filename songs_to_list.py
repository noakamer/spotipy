import os
import json
import const
from artist import Artist
from song import Song
from album import Album


def all_songs_path():
    list_of_all_songs_path = os.listdir(const.SONGS_PATH)
    return list_of_all_songs_path


def all_songs_data(list_of_all_songs_path: list[str]):
    list_of_all_songs_data: list[dict] = []
    for song_path in list_of_all_songs_path:
        file = open(const.SONGS_PATH + const.SLASH + song_path)
        # the data type is a dict
        data = json.load(file)
        list_of_all_songs_data.append(data)
    return list_of_all_songs_data


def artist_exist(artist_data: dict):
    for artist in const.LIST_OF_ARTISTS:
        if artist_data.get(const.ARTISTS).get(const.ID) == artist.get(const.ID):
            return True
    return False


def convert_data_to_object(list_of_all_data: list[dict]):
    is_the_artist_exist = False
    for data in list_of_all_data:
        is_the_artist_exist = artist_exist(data.get(const.ARTISTS))
        if is_the_artist_exist:
            pass
        else:
            artist = Artist(data)
            const.LIST_OF_ARTISTS.append(artist)


l = [{"id": 1, "data": "hi"}, {"id": 2, "data": "bye"}]
print(l[0])
l2 = [1, 2]
for i in l:
    if i.get("id") == 2:
        print(i)
