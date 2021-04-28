#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        if digit1 < digit2 and digit1 != 8:
            print("{:d}{:d}".format(digit1, digit2), end=', ')
        if digit1 < digit2 and digit1 == 8:
            print("{:d}{:d}".format(digit1, digit2))
