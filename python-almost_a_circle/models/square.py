#!/usr/bin/python3
"""
square model using the base blueprint/template
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Our beautiful square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        il constructtoro
        attributes:
            size -> the size of the square(not in inches)
            x -> coord for width
            y -> coord for height
            id -> driver's licence
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size editor
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        """
        changes the output method of the string method
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        updates the same as in rectangle
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, n in enumerate(args):
                if i < len(args):
                    setattr(self, attributes[i], n)
        else:
            for a, b in kwargs.items():
                if hasattr(self, a):
                    setattr(self. a, b)
