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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """save to file"""
        parsed = []
        if list_objs is not None:
            for item in list_objs:
                parsed.append(item.to_dictionary())
            parsed = Base.to_json_string(parsed)

        with open(cls.__name__ + ".json", "w+") as f:
            if list_objs is None:
                f.write("[]")
            else: 
                f.write(parsed)