#!/usr/bin/python3
"""contanins a class Rectangle"""


class Rectangle:
    """Define a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
           parameters:
                width (int): width of the new rectangle
                height (int): height of a rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Is to get it back"""
        return self.__width

    @width.setter
    def width(self, value):
        """It's to configure it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to get it back"""
        return self.__height

    @height.setter
    def height(self, value):
        """to configurate it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
