#!/usr/bin/python3
"""create"""

class MyInt(int):
    """create function"""

    def __eq__(self, other):
        """eq comparation"""
        return int.__ne__(self, other)
   
    def __ne__(self, other):
        """ne comparation"""
        return int.__eq__(self, other)
