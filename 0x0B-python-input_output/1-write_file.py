#!/usr/bin/python3
""" 1-write_file
    write on a file
"""


def write_file(filename="", text=""):
    """write on a file"""
    with open(filename, 'w') as write_file:
        return (write_file.write(text))
