#!/usr/bin/python3
""" 4-inherits_from
    inherits from
"""


def inherits_from(obj, a_class):
    """inherits from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
