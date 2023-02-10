#!usr/bin/python3
"""
A class named rectangle that inherits from BaseGeometry
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
        super().integer_validator(width, "height")
        super().integer_validator("height", width)
        self.__height = height
        self.__width = width