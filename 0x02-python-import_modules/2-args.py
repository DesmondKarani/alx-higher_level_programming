#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude script name itself
    arg_word = "argument" if num_args == 1 else "arguments"

    if num_args == 0:
        print(f"Number of {arg_word}.")
    else:
        print(f"Number of {arg_word}:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
