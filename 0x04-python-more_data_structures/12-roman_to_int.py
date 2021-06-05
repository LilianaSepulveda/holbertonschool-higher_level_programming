#!/usr/bin/python3

# function that converts a roman numeral to an integer


def roman_to_int(roman_string):
    roman_dic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    num = 0
    conv = 0
    for i in roman_string:
        if num < roman_dic[i]:
            conv -= num * 2
        num = roman_dic[i]
        conv += roman_dic[i]
    return conv
