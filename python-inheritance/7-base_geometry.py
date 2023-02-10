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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
