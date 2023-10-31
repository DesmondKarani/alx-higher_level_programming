#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:  # ASCII values for lowercase letters
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Leave non-lowercase characters unchanged
    print(result)

# You can test your function with:
# uppercase('hello world!')  # Should print: HELLO WORLD!
