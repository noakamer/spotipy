import inspect
import os
import json
import const
from log import info_log


def all_songs_path(songs_path):
    list_of_all_songs_path = os.listdir(songs_path)
    call_stack = inspect.stack()
    info_log(__name__, call_stack[0][3], "cast all the song path to list successfully")
    return list_of_all_songs_path


def all_songs_data(list_of_all_songs_path: list):
    list_of_all_songs_data: list = []
    for song_path in list_of_all_songs_path:
        file = open(const.SONGS_PATH + const.SLASH + song_path)
        list_of_all_songs_data.append(json.load(file))
    call_stack = inspect.stack()
    info_log(__name__, call_stack[0][3], "convert list of path to list of songs data successfully")
    return list_of_all_songs_data


