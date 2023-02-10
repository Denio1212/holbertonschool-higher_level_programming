#!/usr/bin/python3
"""
Inheriting a square
"""
Rectangle = __import__("9-rectangle").Rectangle
GeometryBase = __import__("7-base_geometry").BaseGeometry


class Square(Rectangle):
    """
    Just a square m8
    """
    def __init__(self, size):
        """
        initializer
        """
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Area returner
        """
        return self.__size ** 2
