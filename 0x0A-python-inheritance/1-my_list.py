#!/usr/bin/python3
"""This module defines the class MyList"""


class MyList(list):
    """Class MyList inherits from list"""
    def print_sorted(self):
        """Prints list in ascending sorted order"""
        print(sorted(self))
