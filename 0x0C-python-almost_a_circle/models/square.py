#!/usr/bin/python3
"""This module defines the Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize private instance variables using super"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of a square"""
        return "[Square] ({}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Property size: size of square

        setter calls super properties to set width and height to size

        Parameter:
            value: value of size to set width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
