#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """A method that prints the list, but sorted (ascending sort)"""
        print(sorted(self))

