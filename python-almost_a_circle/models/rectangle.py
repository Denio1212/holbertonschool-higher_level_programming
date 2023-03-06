#!/usr/bin/python3
"""
makes an inheritant rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    inherits from the blueprint
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        el constructor
        The arguments:
            width: how wide the rectangle is
            height: its height
            x: coordinate
            y: coordinate
            id: its special id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        assigner of value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        value modifier
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        changing the cords
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("value must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        modifies the y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("value must be > 0")
