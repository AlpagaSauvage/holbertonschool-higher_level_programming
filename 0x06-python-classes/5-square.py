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

    @property
    def size(self):
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif type(self.__size) == int:
            return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif type(value) == int:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        a = self.__size
        b = self.__size
        while b != 0:
            print('#', end="")
            b -= 1
            if a != 1 and b == 0:
                print("")
                a -= 1
                b = self.__size
        print("")
