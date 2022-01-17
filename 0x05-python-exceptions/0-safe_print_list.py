#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = x
    while i != 0:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
            i -= 1
        except:
            print()
            return count
    print()
    return count
