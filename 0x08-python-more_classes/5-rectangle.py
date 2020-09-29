#!/usr/bin/python3
"""create"""


class Rectangle:
    """create a class called Rectangle"""
    def __init__(self, width=0, height=0):
        """private size"""
        self.width = width
        self.height = height

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """return __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setiar a value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setiar a value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """print"""
        texto = ""
        if self.__width > 0 and self.__height > 0:
            for x in range(self.__height):
                texto += "#" * self.__width
                texto += "\n"
        return texto[:-1]

    def __repr__(self):
        """print"""
        return 'Rectangle(' + str(self.__width)\
            + ', ' + str(self.__height) + ')'

    def __del__(self):
        """del method"""
        print("Bye rectangle...")
