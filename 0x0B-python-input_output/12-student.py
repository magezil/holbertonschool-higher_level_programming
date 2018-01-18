#!/usr/bin/python3
"""Module creates class Student"""


class Student:
    """Student class with public instance attributes

    Instance Attributes:
        first_name: first name of student
        last_name: last name of student
        age: age of student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of instance

        Params:
            attrs: attributes to retrieve.
            if not a list of strings, retrieve all attributes
        """
        if not attrs:
            return self.__dict__
        filtered = {}
        for a in attrs:
            value = getattr(self, a, None)
            if value is None:
                continue
            filtered[a] = value
        return filtered
