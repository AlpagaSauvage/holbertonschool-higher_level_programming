#!/usr/bin/python3
"""base.py:
    Base class
"""


import json
from queue import Empty


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or list_dictionaries is Empty:
            return []
        else:
            return json.dumps(list_dictionaries)
