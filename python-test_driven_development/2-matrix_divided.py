#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    """
    if matrix:
        for i in matrix:
            for j in i:
                if type(j) is not float and type(j) is not int:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                if len(i) != len(matrix[0]):
                    raise TypeError("Each row of the matrix must have the same size")
                if type(div) is not int and type(div) is not float:
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i] for i in matrix]
