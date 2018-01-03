#!/usr/bin/python3


class Square:
    """Square class with validated private instance attribute size"""

    def __init__(self, size=0):
        """Args:
               size: size of square
        """
        self.__size = size
