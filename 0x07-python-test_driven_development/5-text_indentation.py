#!/usr/bin/python3
"""
Module defines function text_indentation().
Raises:
    TypeError: if text is not a string
"""


def text_indentation(text):
    """
    Prints text with 2 lines after each `.`, `?`, and `:`
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    start = True
    for c in text:
        if c == " " and start:
            continue
        if c == "." or c == "?" or c == ":":
            print("{}\n".format(c))
            start = True
        else:
            start = False
            print("{}".format(c), end="")
