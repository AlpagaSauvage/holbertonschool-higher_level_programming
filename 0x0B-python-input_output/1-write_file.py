#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as write_file:
        return (write_file.write(text))