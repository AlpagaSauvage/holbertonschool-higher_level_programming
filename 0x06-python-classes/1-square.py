#!/usr/bin/python3
"""Classe Square
    print square with varianble size
"""


class Square:
    """
    define size square

    Attibutes
    ---------
    size : int
        the size of the square.
    """
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int
            the size of the square.
        """
        self.__size = size
