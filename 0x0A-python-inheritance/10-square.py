#!/usr/bin/python3
"""This module creates class Square which inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """Instantiate private instance field size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
