#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size):
        """ Initialize Square with size """
        self.integer_validator("size", size)
        super().__init__(size, size)
