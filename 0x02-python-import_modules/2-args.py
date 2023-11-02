#!/usr/bin/python3
import sys


def main():

    # Subtract 1 to exclude counting script name👇🏿
    num_args = len(sys.argv) - 1
    # Do not include the script name in the count 👇🏿
    print(f"{num_args} argument(s):" if num_args != 1 else "1 argument:")
    for i, arg in enumerate(sys.argv[1:], start=1):  # Start counting from 1
        print(f"{i}: {arg}")


if __name__ == "__main__":
    main()