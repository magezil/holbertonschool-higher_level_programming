#!/usr/bin/python3


class Square:
    """Square class with validated private instance attribute size"""

    def __init__(self, size=0):
        """Args:
               size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __eq__(self, other):
        """Checks if two Squares are equal

        Args:
            other: Square to compare to current instance
        """
        return self.size == other.size

    def __ne__(self, other):
        """Checks if two Squares are not equal

        Args:
            other: Square to compare to current instance
        """
        return self.size != other.size

    def __gt__(self, other):
        """Checks if current Square is greater than other Square

        Args:
            other: Square to compare to current instance
        """
        return self.size > other.size

    def __ge__(self, other):
        """Checks if current Square is greater than or equal to other Square

        Args:
            other: Square to compare to current instance
        """
        return self.size >= other.size

    def __lt__(self, other):
        """Checks if current Square is less than other Square

        Args:
            other: Square to compare to current instance
        """
        return self.size < other.size

    def __le__(self, other):
        """Checks if current Square is less than or equal to other Square

        Args:
            other: Square to compare to current instance
        """
        return self.size <= other.size

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
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of Square instance and returns it"""
        return self.size ** 2
