#!/usr/bin/python3
""" 6-load_from_json_file
    return from json file
"""


import json


def load_from_json_file(filename):
    """ return from jsoon file"""
    with open(filename, 'r') as f:
        return f.read()
