#!/usr/bin/python3
"""
This module defines the function add_integer().
Raises:
    TypeError: if a or b are not a number (integer or float)
"""


def add_integer(a, b):
    """
    Returns the result of a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
