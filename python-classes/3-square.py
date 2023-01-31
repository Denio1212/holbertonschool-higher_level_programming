#!/usr/bin/python3
"""A class with validated size and a public instance"""


class Square:
    'Holds a size and validation for it'
    def __init__(self, size=0):
        'initializer'
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        'Returns the current area of square'
        return self.__size**2
