#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Check if matrix is a valid 2D array
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        return None
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Check if element is an integer
            if isinstance(element, int):
                # Square the element and append it to the new row
                new_row.append(element ** 2)
            else:
                # Return None if element is not an integer
                return None
        # Append the new row to the new matrix
        new_matrix.append(new_row)
    # Return the new matrix
    return new_matrix
