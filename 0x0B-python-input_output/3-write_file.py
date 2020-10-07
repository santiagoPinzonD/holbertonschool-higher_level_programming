#!/usr/bin/python3
"""create"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, mode="w+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
