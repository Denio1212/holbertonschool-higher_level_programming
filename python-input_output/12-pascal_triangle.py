#!/usr/bin/python3
"""
Don't care for this
"""


def factorial(n):
    """
    Returns factorial or whatever
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


def pascal_triangle(n):
    """
    Ye You know it already, this is not woth me even learning now but whatever
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
