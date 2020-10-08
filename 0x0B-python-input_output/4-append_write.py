#!/usr/bin/python3
"""create"""


def append_write(filename="", text=""):
    """write a file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
