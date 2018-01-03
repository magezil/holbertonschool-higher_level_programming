#!/usr/bin/python3


class Square:
    """Square class with validated private instance attribute size"""

    def __init__(self, size=0):
        """Args:
               size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of Square instance and returns it"""
        return __size ** 2
