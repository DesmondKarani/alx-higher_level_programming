#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix or not matrix[0]:
        return []

    # Create a new matrix with squared values using list comprehension
    return [[element ** 2 for element in row] for row in matrix]
