#!/usr/bin/python3
"""This module defines the function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Function checks whether given object is an instance of specified class
    or class that inherted from specified class

    Params:
        obj: object to check
        a_class: class to check against

    Return: True if it is, False otherwise
    """
    return isinstance(obj, a_class)
