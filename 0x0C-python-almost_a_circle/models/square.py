#!/usr/bin/python3
"""square.py:
    print a square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """classe Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init of square"""
        self.size = size
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value <= 0:
            raise ValueError('size must be > 0')
        else:
            self.__size = value

    def __str__(self):
        """ Definition of the square """
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.__x, self.__y, self.__size)
