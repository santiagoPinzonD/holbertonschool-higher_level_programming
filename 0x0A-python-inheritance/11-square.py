#!/usr/bin/python3
"""create"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create a class"""
    def __init__(self, size):
        """init"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.area()

    def __str__(self):
        """__str"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
