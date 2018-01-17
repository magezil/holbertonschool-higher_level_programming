#!/usr/bin/python3
"""Module defines append_write() function"""


def append_write(filename="", text=""):
    """Appends a string to a text file

    Return: the number of characters written

    Param:
        filename: name of text file
        text: string to append
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(str(text))
