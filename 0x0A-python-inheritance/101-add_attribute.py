#!/usr/bin/python3
"""This module defines function add_attribute"""


def add_attribute(obj, attribute, value):
    """Tries to add an attribute to a class

    Raises:
        TypeError: if cannot add attribute
    """
    try:
        setattr(obj, attribute, value)
    except Exception:
        raise TypeError("can't add new attribute")
