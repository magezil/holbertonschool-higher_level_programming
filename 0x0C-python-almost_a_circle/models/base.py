#!/usr/bin/python3
"""This module defines the Base class"""
from random import random
import csv
import json
import turtle


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
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        else:
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Return list of instances from file

        filename is <Class name>.json
        """
        try:
            filename = "{}.json".format(cls.__name__)
            with open(filename, 'r') as f:
                objs = Base.from_json_string(f.read())
                instances = [cls.create(**obj) for obj in objs]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a representations of objects in list to CSV file

        Description"
            Write CSV representation of objects in list_objs to file
            <Class name>.csv

            Parameter:
                list_objs: list of objects
        """
        if cls.__name__ == "Rectangle":
            attrs = ['id', 'width', 'height', 'x', 'y']
        else:
            attrs = ['id', 'size', 'x', 'y']
        filename = "{}.csv".format(cls.__name__)
        if list_objs is not None:
            with open(filename, 'w', newline='') as csvf:
                writer = csv.DictWriter(csvf, fieldnames=attrs)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of instances from file
        filename is <Class name>.csv
        """
        try:
            filename = "{}.csv".format(cls.__name__)
            with open(filename, newline='') as csvf:
                reader = csv.DictReader(csvf)
                obj_list = []
                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    obj_list.append(row)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        shapes = list_rectangles + list_squares
        for shape in shapes:
            fill_color = (random(), random(), random())
            pen_color = (random(), random(), random())
            turtle.color(fill_color, pen_color)
            turtle.setpos((shape.x, shape.y))
            turtle.down()
            turtle.begin_fill()
            for i in range(2):
                turtle.forward(shape.height)
                turtle.left(90)
                turtle.forward(shape.width)
                turtle.left(90)
            turtle.end_fill()
            turtle.up()
