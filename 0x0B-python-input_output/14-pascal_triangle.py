#!/usr/bin/python3
"""Module defines function pascal_triangle()"""


def pascal_triangle(n):
    """Returns list of lists of integers representing Pascal's triangle

    Param:
        n: size of triangle
    """
    if n <= 0:
        return []

    pt = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pt[i-1][j-1] + pt[i-1][j])
        row.append(1)
        pt.append(row)

    return pt
