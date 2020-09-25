#!/usr/bin/python3
"""create"""


def say_my_name(first_name, last_name=""):
    """Create a function that print a name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
