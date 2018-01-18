#!/usr/bin/python3
"""This module defines function append_after()"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into file after each line containing given string

    Params:
        filename: name of file to operate on
        search_string: string to find
        new_string: string to add after lines with matching word
    """
    lines = []
    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding='UTF8') as f:
        for line in lines:
            f.write(line)


#        line = f.readline()
#        while line != '':
#            if search_string in line:
#                print(new_string, file=f, end="", flush=True)
#            line = f.readline()
