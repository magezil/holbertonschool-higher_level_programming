#!/usr/bin/python3
"""This module defines the Base class"""
import json


class Base:
    """Base class has a public instance attribute id

    Description:
        Base class for all other classes in this project and manages the id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize public instance attribute id

        Parameter:
            id: id for instance

        Attributes:
            id: id for instance - assigned either given id (if not None) or
            value of private class attribute __nb_objects + 1
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation of given list

        Parameter:
            list_directories: list of directories to get JSON representation
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of objects in list to file

        Description:
            Writes JSON string representation of objects in list_objs to file
            <Class name>.json

        Parameter:
            list_objs: list of objects
        """
        write_list = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                write_list.append(obj.to_dictionary())
        write_list = Base.to_json_string(write_list)
        with open(filename, 'w') as f:
            f.write(write_list)

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes set"""
        temp = cls(1, 1, 1)
        temp.update(**dictionary)
        return temp
