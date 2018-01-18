#!/usr/bin/python3
"""This module creates class Rectangle which inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """Instantiate private instance field size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns 'unofficial' representation of Square instance"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
