#!/usr/bin/python3
"""Module defines from_json_string() function"""
import json


def from_json_string(my_str):
    """Return object represented by JSON string"""
    return json.loads(my_str)
