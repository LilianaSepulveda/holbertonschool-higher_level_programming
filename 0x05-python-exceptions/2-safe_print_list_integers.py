#!/usr/bin/python3

# function that prints the first x elements of a list and only integers


def safe_print_list_integers(my_list=[], x=0):
    aux = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            aux += 1
        except (ValueError, TypeError):
            continue
    print("")
    return aux
