#!/usr/bin/python3
def remove_char_at(str, n):
    c = len(str)
    i = 0
    pstring = ""
    while c != 0:
        if i != n:
            stro = ord(str[i])
            pstring += chr(stro)
        c -= 1
        i += 1
    return pstring
