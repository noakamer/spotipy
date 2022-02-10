from consolemenu import *
from consolemenu.items import *
from menu import menu_functions


def welcome_menu():
    menu = ConsoleMenu("welcome")
    sign_up = FunctionItem("sign up", lambda: menu_functions.sign_up())
    log_in = FunctionItem("log in", lambda: menu_functions.log_in())
    menu.append_item(sign_up)
    menu.append_item(log_in)
    menu.show()

