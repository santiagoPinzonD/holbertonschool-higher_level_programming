#!/usr/bin/python3
"""funtion with setter"""


class Square:
    """Class"""
    __size = 0

    def __init__(self, size=0):
        """Private size"""
        self.__size = size

    def area(self):
        """Returns the area"""
        return self.__size ** 2

    @property
    def size(self):
        """ define size"""
        return self.__size

    @size.setter
    def size(self, value):
        """area"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
