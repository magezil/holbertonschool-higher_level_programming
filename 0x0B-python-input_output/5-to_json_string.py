#!/usr/bin/python3
"""Module defines function to_json_string()"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of given string object

    Param:
        my_obj: string object to get view JSON representation of
    """
    return json.dumps(my_obj)
