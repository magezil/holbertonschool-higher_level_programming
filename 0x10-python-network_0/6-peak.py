#!/usr/bin/python3
"""
    Defines function find_peak
"""


def find_peak(list_of_integers):
    """
        Function finds peak in unsorted list of integers

        Args:
            list_of_integers: unsorted list of integers
    """
    if not list_of_integers:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    return peak_rec(list_of_integers, 0, size)

def peak_rec(integers, start, end):
    """
        Recursively finds peak in unsorted list of integers

        Args:
            integers: unsorted list of integers
            start: starting index of segment of list
            end: last index + 1 of segment of list
    """
    mid = (end - start) // 2 + start
    current = integers[mid]
    check_prev = mid == 0 or integers[mid - 1] < current
    check_next = mid == len(integers) - 1 or current > integers[mid + 1]
    if check_prev and check_next:
        return current
    if end - start <= 1:
        return None
    if check_prev:
        return peak_rec(integers, mid + 1, end)
    return peak_rec(integers, start, mid)
