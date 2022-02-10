from consolemenu import *
from consolemenu.items import *
from extract_and_transform import load_to_the_relevant_objects, extract
import inspect
from exceptions import UserDoesNotExistException
import const
from log import info_log, error_log
from user import User


def get__user(username: str, password: str):
    for user in const.LIST_OF_USERS:
        if user.username == username and user.password == password:
            return user
    raise UserDoesNotExistException


def log_in():
    print("log in")
    username = input("please enter your username")
    password = input("please enter your password")
    call_stack = inspect.stack()
    func_name = call_stack[0][3]
    try:
        user = get__user(username, password)
        info_log(__name__, func_name, "logged in successfully")
        print("logged in successfully")
        user_menu(user)
    except UserDoesNotExistException:
        error_log(__name__, func_name, "logged in successfully")
        welcome_menu()


def sign_up():
    call_stack = inspect.stack()
    func_name = call_stack[0][3]
    print("sign up")
    username = input("please enter username")
    password = input("please enter password")
    user = User(username, password)
    const.LIST_OF_USERS.append(user)
    info_log(__name__, func_name, "sign up successfully")
    print("sign up successfully")
    user_menu(user)


def welcome_menu():
    menu = ConsoleMenu("welcome")
    signup = FunctionItem("sign up", lambda: sign_up())
    login = FunctionItem("log in", lambda: log_in())
    menu.append_item(signup)
    menu.append_item(login)
    menu.show()


def user_menu(user: User):
    load_to_the_relevant_objects.convert_data_to_object(
        extract.all_songs_data(extract.all_songs_path(const.SONGS_PATH)))
    menu = ConsoleMenu("welcome")
    get_all_artist = FunctionItem("get all artists", lambda: user.get_all_artists())
    get_artist_album = FunctionItem("get artist album by id", lambda: user.get_artist_album(input("enter artist id")))
    get_top_10_songs = FunctionItem("get top artist song", lambda: user.get_top_artist_songs(input("enter artist id")))
    get_all_album_songs = FunctionItem("get all album songs", lambda: user.get_albums_songs(input("enter album id")))
    menu.append_item(get_all_artist)
    menu.append_item(get_artist_album)
    menu.append_item(get_top_10_songs)
    menu.append_item(get_all_album_songs)
    menu.show()
