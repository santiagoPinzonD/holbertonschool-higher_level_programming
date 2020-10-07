#!/usr/bin/python3
"""create"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as f:
        for x in f:
            print(x, end="")
            if nb_lines <= 0 or nb_lines >= len(f.readlines()):
                print(f.readline(), end="")
