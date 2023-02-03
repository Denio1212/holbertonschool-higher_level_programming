#!/usr/bin/python3


def print_square(size):
    """ Prints a square matrix style(ish)
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
