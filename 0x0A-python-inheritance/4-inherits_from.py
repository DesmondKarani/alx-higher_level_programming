#!/usr/bin/python3
"""a function that returns True if the object is an instance of
a class that inherited (directly or indirectly)
from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that
    inherited (directly or indirectly)
    from the specified class

    Args:
        obj: The object to check
        a_class: The class to compare with the type of obj

    Returns:
        True if obj inherits from a_class, otherwise False
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
