#!/usr/bin/python3
"""
Finally a complete rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A new derivative of BaseGeo
    """

    def __init__(self, width, height):
        """
        Famous constructor
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        WIP
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns the object as a nice str
        """
        return "{{}/{}".format(self.__width, self.__height)

    def print(self):
        """
        Prints instead of returning
        """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))