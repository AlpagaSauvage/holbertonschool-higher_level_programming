#!/usr/bin/python3
def no_c(my_string):
    characters = "cC"
    for x in range(len(characters)):
        my_string = my_string.replace(characters[x], "")
    return my_string
