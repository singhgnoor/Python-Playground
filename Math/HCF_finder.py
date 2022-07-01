""" HCF calculator, Using Euclid's Division Algorithm """
from time import sleep


def get_HCF(num1, num2):
    """ Function for finding HCF of 2 numbers, Returns -1 if any of numbers is negative"""
    if num1 < 0 or num2 < 0: return -1

    if num1 > num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1

    if a % b == 0: return b

    # First Step is out Of the loop
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b

    return b


if __name__ == '__main__':
    print("Welcome to the HCF calculator, Using Euclid's Division Algorithm")

    number1 = int(input("Number 1 : "))
    number2 = int(input("Number 2 : "))

    result = get_HCF(number1, number2)

    print(f"HCF of {number1} and {number2} is : {result}")

    print("Thank you for using our service")
    sleep(10)
