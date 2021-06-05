#!/usr/bin/python3

# function that returns the weighted average of all integers tuple


def weight_average(my_list=[]):
    if not isinstance(my_list, list) or my_list == {}:
        return (0)
    a = 0
    b = 0
    for item in my_list:
        a += (item[0] * item[1])
        b += item[1]
    return a / b
