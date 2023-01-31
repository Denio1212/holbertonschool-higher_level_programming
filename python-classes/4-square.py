#!/usr/bin/python3
"""A class with validated size, a public instance, getter and setter"""


class Square:
    'Holds a size and validation for it'
    def __init__(self, size=0):
        'initializer'
        self.size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        'Returns the current area of square'
        return self.__size**2

    @property
    def size(self):
        'getter'
        return self.__size

    @size.setter
    def size(self, new_size):
        'ammender'
        self.__size = new_size
        if type(new_size) != int:
            raise TypeError('size must be an integer')
        if new_size < 0:
            raise ValueError('size must be >= 0')
