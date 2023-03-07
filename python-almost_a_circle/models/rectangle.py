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
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calcs the area of the rectangle and returns it
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle with the character #
        """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        overrides the str method to return the foremost
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        assigns arguments to attributes
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                if i < len(args):
                    if i < len(attributes):
                        setattr(self, attributes[i], e)
        else:
            for a, b in kwargs.items():
                if hasattr(self, a):
                    setattr(self, a, b)

    def to_dictionary(self):
        """
        returns the dict representation of the rectangle
        """
        new_dict = {}

        for idx, key_finder in self.__dict__.items():
            key = idx.split("__")[-1]
            new_dict[key] = key_finder
            return new_dict
