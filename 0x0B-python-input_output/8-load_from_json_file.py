#!/usr/bin/python3
"""This module defines load_from_json_file() function"""
import json


def load_from_json_file(filename):
    """Return created Object from a JSON file

    Param:
        filename: name of JSON file
    """
    with open(filename) as f:
        obj = json.load(f)
    return obj
