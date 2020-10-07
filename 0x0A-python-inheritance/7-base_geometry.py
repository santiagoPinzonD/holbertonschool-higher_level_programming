#!/usr/bin/python3
"""create"""


class BaseGeometry():
    """create a class empty"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) != int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
