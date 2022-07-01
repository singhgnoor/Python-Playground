def next_palindrome(n):
    n = int(n)
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]
if __name__ == "__main__":
    n = int(input("How many numbers you want to enter\n"))
    numbers = []
    for i in range(n):
        try:
            num = int(input(f"Enter value at {i}\n"))
        except:
            print(f"Invalid Input\nnumber not added")
        numbers.append(num)
    # print(numbers)
    a = []
    for i in range(n):
        if numbers[i] > 20:
            numbers[i] = next_palindrome(numbers[i])
    print(numbers)

