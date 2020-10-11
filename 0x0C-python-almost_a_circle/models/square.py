#!/usr/bin/python3
"""create a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """create a class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init of class Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is a representation of print"""
        return "[Square] " + "(" + str(self.id) + ") " + str(self.x)\
            + "/" + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """width getter that is size"""
        return self.width

    @size.setter
    def size(self, size):
        """width setter that is size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """this function receive *args and kwargs
        with *args this assign an argument to each atributtte
        when these are passed trough args.
        with kwargs i use la function setattr that assign
        automatically key/value
        """
        count = 0
        if args:
            for x in args:
                if count == 0:
                    self.id = x
                if count == 1:
                    self.size = x
                if count == 2:
                    self.x = x
                if count == 3:
                    self.y = x
                count += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """create a dict with Rectangle that are
        id, size x, y
        """
        dicts = {}
        dicts['id'] = self.id
        dicts['size'] = self.size
        dicts['x'] = self.x
        dicts['y'] = self.y
        return dicts
