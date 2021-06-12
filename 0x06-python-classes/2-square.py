#!/usr/bin/python3
"""contains a class Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initialize a new Square
        parameters:
            size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size