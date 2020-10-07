#!/usr/bin/python3
"""create"""


def number_of_lines(filename=""):
    """reading a file"""
    with open(filename, encoding="utf-8") as myfile:
        return (len(myfile.readlines()))
