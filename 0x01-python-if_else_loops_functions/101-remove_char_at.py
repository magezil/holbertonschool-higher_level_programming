#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    if n < 0 or n >= len(str):
        return str
    for i in range(n):
        newstr += str[i]
    for i in range(n + 1, len(str)):
        newstr += str[i]
    return newstr
