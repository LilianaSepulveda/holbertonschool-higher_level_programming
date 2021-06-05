#!/usr/bin/python3

# function that replaces all occurrences of an element by another


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] is search:
            new_list[i] = replace
    return new_list
