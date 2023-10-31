#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Get last digit and handle negative numbers
    print("{}".format(last_digit), end='')  # Print last digit without new line
    return last_digit  # Return the value of the last digit

# You can test your function with:
# print_last_digit(1234)  # Should print: 4
# print_last_digit(-1234)  # Should print: 4
