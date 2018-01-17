#!/usr/bin/python3
"""This module defines number_of_lines() function"""


def number_of_lines(filename=""):
    """Returns number of lines in given text file"""
    count = 0
    with open(filename, encoding="UTF8") as f:
        for line in f:
            count += 1
    return count
