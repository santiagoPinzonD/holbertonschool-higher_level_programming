#!/usr/bin/python3
"""create"""


class MyList(list):
    """create a class"""
    def print_sorted(self):
        """create a function print sorted list"""
        new_list = []
        for x in sorted(self):
            new_list.append(x)
        print(new_list)
