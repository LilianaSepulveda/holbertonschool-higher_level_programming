#!/usr/bin/python3

# function that finds the biggest integer of a list


def max_integer(my_list=[]):
    if my_list == "":
        return None
    my_list.sort()
    return my_list[-1]
