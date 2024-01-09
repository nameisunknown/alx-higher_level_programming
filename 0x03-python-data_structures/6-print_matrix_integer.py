#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for col in row:
            if count == (len(row) - 1):
                print("{:d}".format(col), end="\n")
            else:
                print("{:d} ".format(col), end="")
            count = count + 1
