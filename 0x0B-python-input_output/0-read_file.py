#!/usr/bin/python3
""" 0-read_file
    read a file
"""


def read_file(filename=""):
    """ read on a file"""
    with open(filename, 'r') as read_file:
        print(read_file.read())
