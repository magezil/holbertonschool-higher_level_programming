#!/usr/bin/python3
"""This module defines the function inherits_from()"""


def inherits_from(obj, a_class):
    """Function checks if an object is an instance of a class that inherited
    (directly or indirectly) from specified class

    Params:
        obj: object to check
        a_class: class to check against

    Return: True if is an instance, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
