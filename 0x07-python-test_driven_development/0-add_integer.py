#!/usr/bin/python3
""" 0-add_integer
    add integer
"""


def add_integer(a, b=98):
    """add integer"""
    try:
        return int(a + b)
    except:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer")
