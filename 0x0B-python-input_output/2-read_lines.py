#!/usr/bin/python3
"""create"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            print(f.read(), end="")
        for x in range(nb_lines):
             print(f.read(), end="")
