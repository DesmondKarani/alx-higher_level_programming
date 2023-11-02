#!/usr/bin/python3
if __name__ == "__main__":
    import sys


def main():
    num_args = len(sys.argv) - 1  # Do not count the script name as an argument
    print(f"{num_args} argument(s):" if num_args != 1 else "1 argument:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")


main()
