#!/usr/bin/python3
"""Module defines function lookup()"""


def lookup(obj):
    """Returns the list of available attributes and methods of obj
    
    Param:
        obj: object to operate on
    """
    return dir(obj)
