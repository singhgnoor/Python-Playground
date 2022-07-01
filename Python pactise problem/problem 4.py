def next_palindrome(n):
    n = int(n)
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("How many number/s you want to enter :\n"))
    numbers = []
    for i in range(n):
        print(f"Enter the value at {i}")
        number = int(input())
        numbers.append(number)
    # print(numbers)
    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
