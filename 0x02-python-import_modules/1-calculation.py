#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of two numbers."""
    from calculator_1 import add, sub, mul, div

    num1 = 10
    num2 = 5

    print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    print("{} / {} = {}".format(num1, num2, div(num1, num2)))
