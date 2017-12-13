#!/usr/bin/python3
def max_integer(my_list=[]):
    return min(my_list, key=lambda a: -a)
