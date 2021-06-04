#!/usr/bin/python3

# function that finds the biggest integer of a list


def max_integer(my_list=[]):
    my_list.sort()
    if my_list == "":
        return None
    else:
        return my_list[-1]
