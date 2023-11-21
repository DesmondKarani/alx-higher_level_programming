#!/usr/bin/python3
"""A module for square"""


class Square:
    """Class Square that defines a square by its size.

    The size of the square is a private attribute, ensuring that it is only
    accessible and modifiable through controlled means within the class.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
