#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Arguments:
    matrix (list of lists of int/float): The matrix to divide.
    div (int/float): The divisor.

    Returns:
    list: A new matrix with all elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, or
               if rows of the matrix are of different sizes, or
               if div is not a number.
    ZeroDivisionError: If div is zero.
    """

    if not all(isinstance(row, list) for row in matrix) or not
    all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix of integers/floats")

    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
