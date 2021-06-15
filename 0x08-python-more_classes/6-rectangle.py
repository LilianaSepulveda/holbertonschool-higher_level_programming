#!/usr/bin/python3
"""contanins an class taht defines a rectangle"""


class Rectangle:
    """Class Rectangle that defines a rectangle
        Attributes:
            number_of_instances (int): Number of rectangle instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        parameters:
            width (int): width of the new rectangle.
            height (int): height of a new rectangle.
        """
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Is to get width back"""
        return self.__width

    @width.setter
    def width(self, value):
        """It's to configure width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """to get height back"""
        return self.__height

    @height.setter
    def height(self, value):
        """It's to configure height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """return the current rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the current perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """strins representation of the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        aux = []
        for i in range(self.__height):
            [aux.append("#") for j in range(self.__width)]
            if i != (self.__height - 1):
                aux.append("\n")
        return ("".join(aux))

    def __repr__(self):
        """string representation of a rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print message at delete a instance rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
