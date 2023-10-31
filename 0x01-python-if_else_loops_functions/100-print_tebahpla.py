#!/usr/bin/python3
for i in range(122, 96, -1):  # ASCII values from 'z' to 'a'
    print("{}".format(chr(i - 32) if (122 - i) % 2 else chr(i)), end='')
