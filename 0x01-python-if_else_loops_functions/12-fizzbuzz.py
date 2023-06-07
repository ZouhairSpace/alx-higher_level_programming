def fizzbuzz():
    result = ""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result += "FizzBuzz "
        elif number % 3 == 0:
            result += "Fizz "
        elif number % 5 == 0:
            result += "Buzz "
        else:
            result += "{} ".format(number)
    print(result)

fizzbuzz()
