#!/usr/bin/python3

# function that print a dictionary by ordered keys


def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print("{}: {}".format(k, a_dictionary[k]))

