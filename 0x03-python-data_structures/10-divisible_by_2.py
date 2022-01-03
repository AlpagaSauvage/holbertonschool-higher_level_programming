#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = 0
    b = len(my_list)
    new_list = []
    while b > 0:
        if my_list[a] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        b -= 1
        a += 1
    return new_list
