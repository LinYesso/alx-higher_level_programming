#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = [[x ** 2 for x in row] for row in matrix]
    return _matrix
