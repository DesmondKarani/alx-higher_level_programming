#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size):
        """ Initialize Square with size """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """ Return the square description """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
