#!/usr/bin/python3
def fizzbuzz():
    result = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz"
        elif i % 5 == 0:
            result += "Buzz"
        elif i % 3 == 0:
            result += "Fizz"
        else:
            result += str(i)
        result += ' '  # Add a space after each value
    print(result)

fizzbuzz()
