#!/usr/bin/python3
"""This module creates an empty class BaseGeometry"""


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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0". format(name))
