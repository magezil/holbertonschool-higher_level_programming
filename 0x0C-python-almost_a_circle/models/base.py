#!/usr/bin/python3
"""This module defines the Base class"""


class Base:
    """Base class has a public instance attribute id

    Description:
        Base class for all other classes in this project and manages the id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize public instance attribute id

        Parameter:
            id: id for instance

        Attributes:
            id: id for instance - assigned either given id (if not None) or
            value of private class attribute __nb_objects + 1
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
