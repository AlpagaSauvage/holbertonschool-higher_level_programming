#!/usr/bin/python3
from decimal import DivisionByZero
from pickle import NONE
from unittest import expectedFailure


def safe_print_division(a, b):
    result = 0
    try:
        result += (a / b)
        print("Inside result: {:d}.0".format(int(result)))
        print("{:d}".format(result))
    except ZeroDivisionError:
        result = None
        print("Inside result: None")
    finally:
        return result
