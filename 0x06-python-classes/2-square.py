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
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
