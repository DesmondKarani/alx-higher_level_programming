#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if roman_string is a valid string
    if not isinstance(roman_string, str):
        return 0
    # Create a dictionary to store the values of the Roman symbols
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Create a variable to store the result
    result = 0
    # Iterate over the characters of the string
    for i in range(len(roman_string)):
        # Get the value of the current character
        current = roman_values.get(roman_string[i], 0)
        # Get the value of the next character if it exists
        if i + 1 < len(roman_string):
            next = roman_values.get(roman_string[i + 1], 0)
        else:
            next = 0
        # Check if the current value is smaller than the next value
        if current < next:
            # Subtract the current value from the result
            result -= current
        else:
            # Add the current value to the result
            result += current
    # Return the result
    return result
