#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as read_file:
        print(read_file.read())
