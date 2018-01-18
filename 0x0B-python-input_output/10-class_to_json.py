#!/usr/bin/python3
"""Module defines function class_to_json"""
import json


def class_to_json(obj):
    """Returns the dictionary description of simple data structure
    (list, dictionary, string, integer, boolean)

    Return:
        dictionary of given object

    Param:
        obj: instance of a class
    """
    return obj.__dict__
