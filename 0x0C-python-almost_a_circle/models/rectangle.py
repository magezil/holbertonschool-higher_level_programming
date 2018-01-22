#!/usr/bin/python3
"""This module defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base

    Instance properties:
        width: width of Rectangle
        height: height of Rectangle
        x: x position of Rectangle
        y: y position of Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize private instance variables using property"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns string representation of a rectangle"""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Property width: width of rectangle

        setter validates value is an integer > 0

        Parameter:
            value: value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Property height: height of rectangle

        setter validates value is an integer > 0

        Parameter:
            value: value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Property x: x position of rectangle

        setter validates value is an integer >= 0

        Parameter:
            value: value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Property y: y position of rectangle

        setter validates value is an integer >= 0

        Parameter:
            value: value of the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validates a given value is a postive int

        Parameters:
            name: name of variable to validate
            value: value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Return areae of rectangle"""
        return self.height * self.width

    def display(self):
        """Print to stdout the rectangle using #"""
        rectangle = "\n" * self.y
        line = " " * self.x + "#" * self.width + "\n"
        rectangle += (line) * self.height
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Updates no keyword arguments first, then keyword arguments"""
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
            return
        for k, v in kwargs.items():
            setattr(self, k, v)
