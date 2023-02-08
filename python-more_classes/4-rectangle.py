#!/usr/bin/python3
""" Added a redoer
"""


class Rectangle:
    """ A rectangle with a width and height params..
     """
    def __init__(self, width=0, height=0):
        """ Constructor
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height

    @property
    def width(self):
        """ Getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns Perimeter of rectangle
        """
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ Makes the funny hashtags
    """
        seperator = ''
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for place in range(self.__width):
                    seperator += '#'
                seperator += '\n'
        return seperator[: -1]

    def __repr__(self):
        """ Evaluates string using eval command
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
