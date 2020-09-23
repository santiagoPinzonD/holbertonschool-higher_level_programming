#!/usr/bin/python3
"""Class that define as the point zero"""


class Square:
    """Class square"""
    __size = 0
    __position = ()

    def __init__(self, size=0, position=(0, 0)):
        """Private size"""
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """ define size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define area"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print area"""
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            print(" ", end="")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """define position"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(self.__position) is not 2 and type(self.__position) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
