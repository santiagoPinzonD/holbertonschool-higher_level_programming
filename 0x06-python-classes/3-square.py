#!/usr/bin/python3
"""funtion that define the area"""


class Square:
    """Class"""
    __size = 0

    def __init__(self, size=0):
        """Private"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return area to square"""
        return self.__size ** 2
