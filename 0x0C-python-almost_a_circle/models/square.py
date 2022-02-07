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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ Definition of the square """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.__x, self.__y, self.size)

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
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return the dictionnary of Rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
