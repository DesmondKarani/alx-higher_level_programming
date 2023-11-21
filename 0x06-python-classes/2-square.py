#!/usr/bin/python3
"""
This module provides the 'Square' class which defines a square by its size.
The size attribute of the square is validated to ensure it's an integer and
non-negative. This implementation is part of a Python learning project.
"""


class Square:
    """
    Class Square that defines a square by its size, ensuring the size is an
    integer and non-negative. This class is part of a learning project and
    serves as an introduction to object-oriented programming in Python.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
