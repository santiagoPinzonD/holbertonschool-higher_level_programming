#!/usr/bin/python3
"""create"""


def read_lines(filename="", nb_lines=0):
    """read lines"""
    nlines = len(open(filename).readlines())
    with open(filename, encoding="utf-8") as f:
        if nb_lines > 0 and nb_lines < nlines:
            for lines in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
