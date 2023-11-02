#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4


def print_hidden_names():
    names = dir(hidden_4)  # Get a list of names from the hidden_4 module
    for name in sorted(names):  # Sort and iterate over the list
        if not name.startswith('__'):  # Filter out names starting with '__'
            print(name)

    print_hidden_names()
