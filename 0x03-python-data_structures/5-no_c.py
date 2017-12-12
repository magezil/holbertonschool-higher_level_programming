#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    C = ord("C")
    c = ord("c")
    for s in my_string:
        if ord(s) != C and ord(s) != c:
            new_string += s
    return new_string
