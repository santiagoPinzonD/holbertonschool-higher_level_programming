#!/usr/bin/python3
"""create"""


def text_indentation(text):
    """create a function"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for x in text:
        if x == "." or x == "?" or x == ":":
            print(x)
            print()
        else:
            print(x, end="")
