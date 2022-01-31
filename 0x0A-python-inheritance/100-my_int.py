#!/usr/bin/python3
"""100-my_int.py:
    my int
"""


class MyInt(int):
    """MyInt"""
    def __eq__(self, other):
        return int.__index__ == other

    def __ne__(self, other):
        return int.__index__ != other
