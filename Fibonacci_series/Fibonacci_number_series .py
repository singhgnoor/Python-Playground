""" Class 11 Final IP Practice 2021, Fibonacci Series"""
from time import sleep


def get_Fibonacci_series(nTerms):
    term1, term2 = (0, 1)
    if nTerms <= 0:
        print("Please Enter a Positive Integer(natural number).")
        return -1

    elif nTerms == 1:
        return [term1]

    else:
        count = 0
        ret_list = []
        while count < nTerms:
            ret_list.append(term1)
            sum_of_terms = term1 + term2
            # update values
            term1 = term2
            term2 = sum_of_terms
            count += 1
        return ret_list


if __name__ == '__main__':
    print("Welcome to the Fibonacci numbers Series finder!")
    number_of_Terms = int(input("How Many terms you want? - "))
    result = get_Fibonacci_series(number_of_Terms)

    print("Fibonacci Series - ")
    if result != -1:
        index = 0
        while index < number_of_Terms:
            print(f"{index + 1}. {result[index]}")
            index += 1

    print("Thank you for using our service!")
    sleep(10)
