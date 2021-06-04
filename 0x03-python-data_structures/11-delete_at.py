#!/usr/bin/python3

# function that deletes the item at specific position in a list


def delete_at(my_list=[], idx=0):
    del (my_list[idx])
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list
