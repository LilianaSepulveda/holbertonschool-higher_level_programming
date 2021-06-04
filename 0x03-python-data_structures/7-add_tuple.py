#!/usr/bin/python3

# function that adds 2 tuples


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return tuple(map(sum, zip(a[:2], b[:2])))
