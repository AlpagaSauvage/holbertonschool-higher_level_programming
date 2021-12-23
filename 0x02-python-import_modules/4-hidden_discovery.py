#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    a = dir(hidden_4)
    c = len(dir(hidden_4))
    i = 0
    while i != c:
        if a[i][1] != '_':
            print(a[i])
        i += 1
