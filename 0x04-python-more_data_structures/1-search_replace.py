#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = len(my_list)
    new_list = my_list[:]
    c = 0
    while i != 0:
        if my_list[c] == search:
            new_list[c] = replace
        i -= 1
        c += 1
    return new_list
