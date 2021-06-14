#!/usr/bin/python3
"""contains a class Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square
        parameters:
            size (int): size of the new square
            position (int, int): position of a square,
            tuple of 2 positive integers
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """to get it back"""
        return self.__position

    @position.setter
    def position(self, value):
        """to configurate it"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(num >= 0 for num in value) or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print the square with the # character"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
