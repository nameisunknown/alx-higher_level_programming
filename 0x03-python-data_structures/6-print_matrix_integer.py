#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        count = 0
        for l in li:
            if count == (len(li) - 1):
                print("{}".format(l), end="\n")
            else:
                print("{} ".format(l), end="")
            count = count + 1
    print("--")
