#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
last_digit = number % 10

# Adjust for negative numbers
if number < 0 and last_digit != 0:
    last_digit -= 10

# Print the initial part of the message
print("Last digit of {} is {}".format(number, last_digit), end=" ")

# Print the appropriate message based on the value of the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
