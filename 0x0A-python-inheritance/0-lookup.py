#!/usr/bin/python3
"""defines an object attribute lookup function"""


def lookup(obj):
    """returns the list of attributes and methods of an object"""
    list = []

    for i in dir(obj):
        list.append(i)

    return list
