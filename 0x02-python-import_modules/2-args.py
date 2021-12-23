#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        length = len(sys.argv)
        if length == 2:
            print("{} argument:".format(length - 1))
        else:
            print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
