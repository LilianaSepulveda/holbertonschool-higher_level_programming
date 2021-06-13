#!/usr/bin/python3
"""contains a class Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initialize a new Square
        parameters:
            size (int): size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Is to get it back"""
        return self.__size

    @size.setter
    def size(self, value):
        """It's to configure it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def my_print(self):
        for i in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
