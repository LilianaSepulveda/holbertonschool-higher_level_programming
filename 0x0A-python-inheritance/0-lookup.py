#!/usr/bin/python3
"""defines an object attribute lookup function"""


def lookup(obj):
    """returns the list of attributes and methods of an object"""
    return dir(obj)