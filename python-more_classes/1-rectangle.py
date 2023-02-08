#!/usr/bin/python3
""" Makes a rectangle with some parametres 
"""

class Rectangle:
    """ A rectangle with a width and height params..
     """
    def __init__(self,  width=0, height=0):
        """ Constructor """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
             self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value  < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
