#!/usr/bin/python3
"""function that returns dictionary description with simple data structure"""


def class_to_json(obj):
    """ Returns the dictionary description for JSON serialization
    of an object """
    return obj.__dict__
