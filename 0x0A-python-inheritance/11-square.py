#!/usr/bin/python3
"""This module creates class Rectangle which inherits from BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Raises an Exception - method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a given value is a positive int

        Param:
            name: name of variable to validate
            value: value to validate

        Raises:
            TypeError: if value is not an int
            ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0". format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiate private instance fields width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns 'unofficial' representation of Rectangle instance"""
        name = type(self).__name__
        return "[{}] {:d}/{:d}".format(name, self.__width, self.__height)

    def area(self):
        """Returns area of Rectangle instance"""
        return self.__width * self.__height


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """Instantiate private instance field size"""
        super().__init__(size, size)
        self.__size = size
