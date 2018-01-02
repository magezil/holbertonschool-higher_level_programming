#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
        print("")
    except IndexError:
        print("")
    return i
