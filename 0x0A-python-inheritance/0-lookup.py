#!/usr/bin/python3
"""defines attributes and methods of lookup function."""


def lookup(obj):
    """return a list of attributes and methods of a object"""

    list_obj = []

    for i in dir(obj):
        list_obj.append(i)

    return list_obj
