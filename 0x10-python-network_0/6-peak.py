#!/usr/bin/python3
"""Finds a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Peak in a list unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
