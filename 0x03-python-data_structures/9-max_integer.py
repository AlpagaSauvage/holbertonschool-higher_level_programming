#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    d = len(my_list)
    c = 0
    i = 0
    while d > 0:
        if my_list[i] > c:
            c = my_list[i]
        i += 1
        d -= 1
    return c
