import inspect
import os
import json
import const
from log import debug_log, info_log, warning_log, error_log


def all_songs_path():
    # TODO should get the const as value to func
    list_of_all_songs_path = os.listdir(const.SONGS_PATH)
    call_stack = inspect.stack()
    func_name = call_stack[0][3]
    info_log(__name__, func_name, "cast all the song path to list successfully")
    return list_of_all_songs_path


def all_songs_data(list_of_all_songs_path: list):
    list_of_all_songs_data: list = []
    for song_path in list_of_all_songs_path:
        file = open(const.SONGS_PATH + const.SLASH + song_path)
        # the data type is a dict
        data = json.load(file)
        list_of_all_songs_data.append(data)
    call_stack = inspect.stack()
    func_name = call_stack[0][3]
    info_log(__name__, func_name, "convert list of path to list of songs data successfully")
    return list_of_all_songs_data


