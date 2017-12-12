#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first = True
        for j in row:
            if not first:
                print(" ", end="")
            else:
                first = False
            print("{:d}".format(j), end="")
        print("")
