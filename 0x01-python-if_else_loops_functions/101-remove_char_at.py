#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):  # Check if n is out of bounds
        return str  # Return the original string if n is out of bounds
    elif n == 0:
        return str[1:]  # Return the string without the first character
    else:
        return str[:n] + str[n+1:]  # Concatenate parts before n after index n

# Example Usage:
result = remove_char_at("Hello, World!", 0)
print(result)  # Output: "ello, World!"
