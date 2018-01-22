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
