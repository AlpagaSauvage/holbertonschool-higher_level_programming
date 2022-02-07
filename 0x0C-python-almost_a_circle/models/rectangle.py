#!/usr/bin/python3
"""rectangle.py:
    print a rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Parameters
        ----------
        size : width, height
            the size of the rectangle.
        """
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

        if id is not None:
            self.id = id
        else:
            super().__init__(id)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        c = self.__y
        while c != 0:
            print("")
            c -= 1
        if self.__width == 0 or self.__height == 0:
            return ""
        print((" " * self.__x + "#" * self.__width + "\n") *
            (self.__height - 1) + " " * self.__x + "#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
