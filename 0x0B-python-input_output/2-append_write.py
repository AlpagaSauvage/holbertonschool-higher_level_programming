#!/usr/bin/python3
""" 2-append_write
    append on a file
"""


def append_write(filename="", text=""):
    """append on end of  a file"""
    with open(filename, 'a') as append_file:
        return (append_file.write(text))
