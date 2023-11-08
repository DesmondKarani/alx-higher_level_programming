#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Check if my_list is a valid list and number is a valid number
    if not isinstance(my_list, list) or not isinstance(number, (int, float)):
        return None
    # Use map to apply a lambda function that multiplies each element by number
    return list(map(lambda x: x * number, my_list))
