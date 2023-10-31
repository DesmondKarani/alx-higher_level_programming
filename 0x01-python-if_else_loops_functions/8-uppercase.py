#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:  # ASCII values for lowercase letters
            print(chr(ord(char) - 32), end='')  # Convert to uppercase
        else:
            print(char, end='')  # Non-lowercase characters remain the same
    print()  # New line
