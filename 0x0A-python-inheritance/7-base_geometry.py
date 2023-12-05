#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with the message that
        the method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
