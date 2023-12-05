#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """ Class that inherits from list """

    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort) """
        print(sorted(self))
