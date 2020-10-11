#!/usr/bin/python3
"""create a class"""
from models.base import Base


class Rectangle(Base):
    """create a class called rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init of class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """function that calculate area"""
        return self.__width * self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ recuperar y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        """show in display the height for the width and
        take care of y that is a newline and x is a space
        """
        print("\n" * self.y, end="")
        for x in range(self.__height):
            print(" " * self.x, end="")
            for z in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """this is a representation of print"""
        return "[Rectangle] " + "(" + str(self.id) + ") " + str(self.__x)\
            + "/" + str(self.__y) + " - " + str(self.__width)\
            + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """this function receive *args and kwargs
        with *args this assign an argument to each atributtte
        when these are passed trough args.
        with kwargs i use la function setattr that assign
        automatically key/value
        """
        count = 0
        count1 = 0
        if args:
            for x in args:
                if count == 0:
                    self.id = x
                if count == 1:
                    self.__width = x
                if count == 2:
                    self.__height = x
                if count == 3:
                    self.__x = x
                if count == 4:
                    self.__y = x
                count += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """create a dict with Rectangle that are
        id, width, height, x, y
        """
        dicts = {}
        dicts['id'] = self.id
        dicts['width'] = self.__width
        dicts['height'] = self.__height
        dicts['x'] = self.__x
        dicts['y'] = self.__y
        return dicts
