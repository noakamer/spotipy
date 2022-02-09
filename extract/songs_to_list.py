import os
import json
import const


def all_songs_path():
    list_of_all_songs_path = os.listdir(const.SONGS_PATH)
    return list_of_all_songs_path


def all_songs_data(list_of_all_songs_path: list):
    list_of_all_songs_data: list = []
    for song_path in list_of_all_songs_path:
        file = open(const.SONGS_PATH + const.SLASH + song_path)
        # the data type is a dict
        data = json.load(file)
        list_of_all_songs_data.append(data)
    return list_of_all_songs_data


