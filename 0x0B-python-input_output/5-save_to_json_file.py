#!/usr/bin/python3
""" 5-save_to_json_file
    save object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """save object to a file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
