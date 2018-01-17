#!/usr/bin/python3
"""This module defines read_file() function"""


def read_file(filename=""):
    """This function reads a text file in UTF8 encoding and prints it

    Param:
        filename: name of file to read from
    """
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end="")
