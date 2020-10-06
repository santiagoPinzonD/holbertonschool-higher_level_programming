#!/usr/bin/python3
"""create"""


def inherits_from(obj, a_class):
    """create function for validate"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
