#!/usr/bin/python3
""" 7-add_item
    add list python to json file
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(arg):
    """ass list python to json file"""
    with open('add_item.json', 'a+'):
        list = load_from_json_file('add_item.json')
        c = 1
        i = len(arg) - 1
        while i != 0:
            list.append(arg[c])
            c += 1
            i -= 1
        save_to_json_file(list, 'add_item.json')


add_item(sys.argv)
