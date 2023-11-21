#!/usr/bin/python3
"""
This module provides the 'Square' class which defines a square by its size
and allows calculating its area. The size attribute of the square is
validated to ensure it's an integer and non-negative.
"""


class Square:
    """
    Class Square that defines a square by its size, ensuring the size is an
    integer and non-negative. Provides a method to calculate the area of the
    square.
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

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
