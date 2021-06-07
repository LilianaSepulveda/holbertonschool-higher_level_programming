#!/usr/bin/python3

# function that divides 2 integers and print the result


def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
