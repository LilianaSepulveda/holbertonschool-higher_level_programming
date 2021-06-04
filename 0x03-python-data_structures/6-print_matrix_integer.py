#!/usr/bin/python3

# Function that prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        print(" ".join(["{:d}".format(i) for i in element]))
