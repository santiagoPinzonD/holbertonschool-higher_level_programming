#!/usr/bin/python3
"""create function"""


def matrix_divided(matrix, div):
    """create function that divide elements of a matrix"""
    new_matrix = []
    if matrix:
        for x in range(0, len(matrix)):
            new_matrix.append([])
            for z in matrix[x]:
                if type(z) != int and type(z) != float:
                    raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                if len(matrix[x]) != len(matrix[0]):
                    raise TypeError("Each row of the matrix must\
 have the same size")
                if type(div) != int and type(div) != float:
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                new_matrix[x].append(round(z / div, 2))
        return new_matrix
    raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
