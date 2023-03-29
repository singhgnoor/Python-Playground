""" Simple python script to Play Guess the number"""
from random import randint


def main(upperLimit=100) -> int:
    num = randint(0, upperLimit)
    guess_number = 1
    while True:
        guess = int(input("What is your Guess on Number : "))
        if guess == num:
            print("Whoa! Correct guess", end=", ")
            if guess_number == 1:
                print("First try!!")
            elif guess_number == 2:
                print("Second try!")
            elif guess_number == 3:
                print("Third try!!")
            else:
                print(f"{guess_number} try.")
            break
        elif guess > num:
            print("Guess a little smaller")
        else:
            print("Guess a little higher")
        guess_number += 1

    return guess_number


if __name__ == '__main__':
    upper_limit_ = 100
    print(f"Welcome to the number guessing game, Here you have to guess a number between 0 and {upper_limit_}")
    print("Now enjoy the game")
    main()
