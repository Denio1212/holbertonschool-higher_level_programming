#!/usr/bin/python3
"""A class with validated size, a public instance, getter and setter"""


class Square:
    'Holds a size and validation for it'
    def __init__(self, size=0, position=[0, 0]):
        'initializer'
        self.__size = size
        self.__position = position
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
    
    @property
    def position(self):
        'getter'
        return self.__position
    
    @position.setter
    def position(self, value):
        'ammender'
        if type(value) != int or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif any(type(i) != int for i in self.__position) or any(j < 0 for j in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif any(type(j) != int for j in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        'Prints the size of square in stdout'
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

