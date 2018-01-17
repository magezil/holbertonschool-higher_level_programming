#!/usr/bin/python3
"""Module defines class MyInt"""


class MyInt(int):
    """Class MyInt is a rebel and inverts == and !="""
    def __eq__(self, other):
        """Returns opposite of what int eq() would return"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Returns opposite of what int ne() would return"""
        return not super().__ne__(other)
