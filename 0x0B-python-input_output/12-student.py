#!/usr/bin/python3
"""create a class"""


class Student():
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """tha same that 10"""
        if attrs is None:
            return self.__dict__
        list1 = {}
        for k, v in self.__dict__.items():
            if k in attrs:
                list1[k] = v
        return list1
