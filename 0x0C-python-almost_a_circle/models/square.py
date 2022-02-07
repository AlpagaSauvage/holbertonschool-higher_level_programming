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
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__size = value

    def __str__(self):
        """ Definition of the square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.__x, self.__y, self.__size)

    def update(self, *args, **kwargs):
        """update"""
        if len(args):
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.height = kwargs["x"]
            if "y" in kwargs:
                self.x = kwargs["y"]
