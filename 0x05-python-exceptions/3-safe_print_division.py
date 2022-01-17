#!/usr/bin/python3
from decimal import DivisionByZero
from pickle import NONE
from unittest import expectedFailure


def safe_print_division(a, b):
    result = 0
    try:
        result += (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(str(result)))
        return result
