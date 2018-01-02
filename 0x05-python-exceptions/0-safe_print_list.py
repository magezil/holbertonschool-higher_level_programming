#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list:
        return 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        i += 1
        if i > 0:
            print()
    except IndexError:
        print()
    return i
