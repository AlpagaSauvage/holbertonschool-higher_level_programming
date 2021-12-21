#!/usr/bin/python3
i = 0
c = 122
e = 89
while i != 26:
    if i % 2 == 0:
        print("{}".format(chr(c)), end="")
        c -= 2
    else:
        print("{}".format(chr(e)), end="")
        e -= 2
    i += 1