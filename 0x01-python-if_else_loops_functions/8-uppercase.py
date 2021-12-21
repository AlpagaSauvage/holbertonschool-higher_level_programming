#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    c = i
    i = 0
    while c != 0:
        if ord(str[i]) in range(97, 123):
            stro = ord(str[i]) - 32
        else:
            stro = ord(str[i])
        print("{}".format(chr(stro)), end="")
        i += 1
        c -= 1
    print("")
