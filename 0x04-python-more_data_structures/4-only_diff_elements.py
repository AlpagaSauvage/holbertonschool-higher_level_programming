#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a_set = set_1
    b_set = set_2
    return (a_set ^ b_set)
