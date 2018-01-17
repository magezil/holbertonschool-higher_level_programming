#!/usr/bin/python3
"""Module defines write_file() function"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Return: the number of characters written

    Param:
        filename: name of text file
        text: string to write
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(str(text))
