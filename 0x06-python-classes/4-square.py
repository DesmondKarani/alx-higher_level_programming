#!/usr/bin/python3
"""
This module provides the 'Square' class which defines a square by its size
and allows calculating its area. It includes a getter and setter for the size
attribute to control its access and validation.
"""


class Square:
    """
    Class Square that defines a square by its size, ensuring the size is an
    integer and non-negative. Includes a getter and setter for the size
    attribute for controlled access and validation.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
