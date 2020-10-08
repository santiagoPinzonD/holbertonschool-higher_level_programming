#!/usr/bin/python3
"""create a class"""


class Student():
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """tha same that 10"""
        return self.__dict__
