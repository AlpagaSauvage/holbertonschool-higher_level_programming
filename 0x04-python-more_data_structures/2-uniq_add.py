#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    d = 0
    c = len(my_list)
    new_list = []
    while c != 0:
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
            d += my_list[i]
        i += 1
        c -= 1
    return d
