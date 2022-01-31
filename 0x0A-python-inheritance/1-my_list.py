#!/usr/bin/python3
"""1-my_list.py:
    my list
"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        print(sorted(self))
