#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    c = 0
    i = x
    while i != 0:
        try:
            print("{:d}".format(my_list[c]), end="")
            count += 1
            c += 1
            i -= 1
        except ValueError:
            c += 1
            i -= 1
        except TypeError:
            c += 1
            i -= 1
    print()
    return count
