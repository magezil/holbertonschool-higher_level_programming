#!/usr/bin/python3
"""This module defines function add_attribute"""


def add_attribute(obj, attribute, value):
    """Tries to add an attribute to a class

    Raises:
        TypeError: if cannot add attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
