#!/usr/bin/python3
"""create"""


class BaseGeometry():
    """create a class empty"""
    def area(self):
        """create a pass area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """create a class"""
    def __init__(self, width, height):
        """init of function"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """create a function of area"""
        return self.__width * self.__height

    def print(self):
        """print function"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """__str"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)