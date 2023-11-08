#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # Check if matrix is a valid 2D array
    if not isinstance(matrix, list) or not all(isinstance(row, list) \
            for row in matrix):
        return None
    # Use map to apply a lambda function that squares each element of each row
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
