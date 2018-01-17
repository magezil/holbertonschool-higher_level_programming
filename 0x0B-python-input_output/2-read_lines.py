#!/usr/bin/python3
"""This module defines read_lines() function"""


def read_lines(filename="", nb_lines=0):
    """Reads and prints given number of lines of a text file

    Reads entire file if given number of lines is negative, zero, or
    greater than or equal to the number of lines in the file

    Param:
        filename: name of file to read from
        nb_lines: number of lines to read
    """
    count = 0
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end="")
            count += 1
            if (count == nb_lines):
                break
