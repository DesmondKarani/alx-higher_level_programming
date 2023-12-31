#!/usr/bin/python3
"""a function that returns True"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class

    Args:
        obj: The object to check
        a_class: The class to match the type of obj

    Returns:
        True if obj is exactly an instance of a_class, otherwise False
    """
    return type(obj) is a_class
