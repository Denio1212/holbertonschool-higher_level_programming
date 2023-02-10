#!/usr/bin/python3
"""
More stuff
"""


class BaseGeometry:
    """
    A class with an aream method
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not str:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
