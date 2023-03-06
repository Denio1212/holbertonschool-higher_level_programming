#!/user/bin/python3
"""
The base class that will be the blueprint
"""


class Base:
    """
    blueprint for classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
