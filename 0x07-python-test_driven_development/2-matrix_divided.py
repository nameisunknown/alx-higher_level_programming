#!/usr/bin/python3

"""
The module is aimed at understanding testing better
The module contains a matrix divided function
"""


def matrix_divided(matrix, div):
    """This functions divides all element of a matrix by a value provided

    Args:
        matrix (list): A variable containing the list to be divided
        div (int): the value to divide each element of the matrix with.

    Returns:
        A list of the divided matrix
    
    Raises:
        TypeError: raise error if div val to be divided with isn't int or float
        ZeroDivisionError: raise error if value entered for div is 0

    """

    type_err_value = "matrix must be a matrix (list of lists of integers/floats"
    each_rowcount = []
    returned_matrix = []

    for loop in matrix:
        for i in loop:
            if not isinstance(i, (int, float)):
                raise TypeError(type_err_value)

    loop = 0
    while loop < len(matrix):
        loop_in = 0
        count_rowlen = 0
        while loop_in < len(matrix[loop]):
            count_rowlen += 1
            loop_in += 1
        each_rowcount.append(count_rowlen)
        loop += 1
    for elem in each_rowcount[1:]:
        if elem != each_rowcount[0]:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for loop_mtrx_row in matrix:
        temp_row = []
        for loop_inside in loop_mtrx_row:
            result = loop_inside / div
            result = round(result, 2)
            temp_row.append(result)
        returned_matrix.append(temp_row)

    return returned_matrix
