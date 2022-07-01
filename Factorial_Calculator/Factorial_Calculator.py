""" This file will help in calculating Factorial of a number """
import math


def factorial_calculator(number):
    """ This function helps to calculate factorial of a number."""

    if number < 0:
        return -factorial_calculator(math.sqrt(number ** 2))

    elif number == 1:
        return 1

    else:
        count = 0
        product = 1
        while count < number:
            product *= count + 1
            count += 1
        return product


if __name__ == '__main__':
    print("Welcome to factorial calculator!")

    num = int(input("What is the number to find factorial - "))

    result = factorial_calculator(num)
    
    print(f"{num}! is {result}")

