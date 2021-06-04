#!/usr/bin/python3

# function that return a tuple with length and first character of a string


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
