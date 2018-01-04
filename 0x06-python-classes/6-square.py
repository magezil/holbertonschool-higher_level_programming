#!/usr/bin/python3


class Square:
    """Square class with validated private instance attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Args:
               size: size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size: size of square

        setter validates size is an integer and >= 0

        Raises:
            TypeError: If size is not an int
            ValueError: If size is < 0
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """position: position of the square

        setter validates that position is a tuple of 2 positive integers

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of Square instance and returns it"""
        return self.size ** 2

    def my_print(self):
        """Prints to stdout the square with # or an empty line if size is 0,
        position indicated by spaces and new lines
        """
        if self.size == 0:
            print("")
        for i in range(self.position[1]):
            print("")
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
