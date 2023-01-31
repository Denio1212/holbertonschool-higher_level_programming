#!/usr/bin/python3
"""A class with validated size"""


class Square:
    'Holds a size and validation for it'
    def __init__(self, size=0):
        'initializer'
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
