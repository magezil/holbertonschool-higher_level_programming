#!/usr/bin/python3


class MagicClass:
    """Magic class that does the same as given bytecode (Circle)"""
    def __init__(self, radius=0):
        """Initialize radius

        Args:
            radius: radius of circle

        Raises:
            TypeError: If radius is not an int nor a float
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Returns the calculated area of circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the calculated circumference of circle"""
        return 2 * math.pi * self.__radius
