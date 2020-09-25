#!/usr/bin/python3
"""Create"""


def print_square(size):
    """create a function that print #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(0, size):
        for z in range(0, size):
            print("#", end="")
        print()
