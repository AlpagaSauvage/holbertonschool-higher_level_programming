#!/usr/bin/python3
""" 8-class_to_json
    class to json
"""


import json


def class_to_json(obj):
    """class to json"""
    return obj.__dict__
