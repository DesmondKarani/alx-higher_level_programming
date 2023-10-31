#!/usr/bin/python3

def fizzbuzz():
    for number in range(1, 101):  # Numbers from 1 to 100
        if number % 3 == 0 and number % 5 == 0:  # Multiples of both three and five
            print("FizzBuzz", end=' ')
        elif number % 3 == 0:  # Multiples of three
            print("Fizz", end=' ')
        elif number % 5 == 0:  # Multiples of five
            print("Buzz", end=' ')
        else:
            print("{}".format(number), end=' ')  # Other numbers

# You can call your function with:
# fizzbuzz()
