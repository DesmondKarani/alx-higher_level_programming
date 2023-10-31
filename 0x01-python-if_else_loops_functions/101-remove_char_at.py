#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):  # Check if n is out of bounds
        return str  # Return the original string if n is out of bounds
    return str[:n] + str[n+1:]  # Concatenate the parts of the string before and after index n

# Example Usage:
result = remove_char_at("Hello, World!", 7)
print(result)  # Output: "Hello World!"
