#!/usr/bin/python3
"""returns True if the object is an instance of,
or if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an
    instance of a class
    that inherited from, the specified class

    Args:
        obj: The object to check
        a_class: The class to compare with the type of obj

    Returns:
        True if obj is an instance or inherits from a_class, otherwise False
    """
    return isinstance(obj, a_class)
