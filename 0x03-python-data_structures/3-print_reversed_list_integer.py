#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list) - 1
    if a < 0:
        return None
    while a >= 0:
        print("{:d}".format(int(my_list[a])))
        a -= 1
