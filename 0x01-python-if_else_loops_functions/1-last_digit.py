#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of number by using modulo 10
last_digit = abs(number) % 10

# Print the first part of the message
print(f"Last digit of {number} is", end=" ")

# Check the value of the last digit and print the corresponding message
if last_digit > 5:
    print(f"{last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit} and is 0")
else:
    print(f"{last_digit} and is less than 6 and not 0")
