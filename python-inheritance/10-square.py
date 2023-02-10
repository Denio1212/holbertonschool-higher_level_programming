#!/usr/bin/python3
"""
Inheriting a square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Just a square m8
    """
    def __init__(self, size):
        """
        initializer
        """
        super().integer_validator("size", size)
        self.__size = size