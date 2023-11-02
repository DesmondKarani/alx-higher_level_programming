#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def main():
        sum_of_args = sum(int(arg) for arg in sys.argv[1:])
        print(sum_of_args)

main()
