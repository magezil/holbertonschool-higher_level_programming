#!/usr/bin/python3
"""This module defines the function is_same_class()"""


def is_same_class(obj, a_class):
    """Function checks whether given object is an instance of specified class

    Return: True if it is, False otherwise
    """
    return type(obj) == a_class
