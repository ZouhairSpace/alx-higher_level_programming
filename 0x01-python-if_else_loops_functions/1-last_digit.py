#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    absolute_number = number * -1
    last_digit = absolute_number % 10
    last_digit = last_digit * -1
else:
    last_digit = number % 10

print("Last digit of {}".format(number), end=' ')

if last_digit > 5:
    print("is {} and is greater than 5".format(last_digit))
elif last_digit == 0:
    print("is {} and is 0".format(last_digit))
elif last_digit < 6 and last_digit != 0:
    print("is {} and is less than 6 and not 0".format(last_digit))

