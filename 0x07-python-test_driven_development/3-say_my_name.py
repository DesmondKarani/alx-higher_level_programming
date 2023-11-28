#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints a person's name in the format "My name is <first name> <last name>".

    Arguments:
    first_name (str): The first name.
    last_name (str): The last name.

    Raises:
    TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
