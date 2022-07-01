from random import randint


def gen_randon_num(a, b):
    if a < b:
        d = randint(a, b)
    else:
        d = randint(b, a)
    return d


def guess_num(name, n):
    i = 1
    print(f"{name}")
    while True:
        print(f"Trial number {i}")
        a = int(input("Guess the number\n"))
        if a == n:
            if i > 1:
                print(f"Congratulations You guessed it in {i} tries")
                break
            else:
                print(f"Congratulations You guessed it in {i} tries")
                break
        elif a > n:
            print("You guessed greater number")
        elif a < n:
            print("You guessed a smaller number")
        i = i + 1
    return i


def winner(a, b):
    if a == b:
        print("Tie")
    elif a > b:
        print("Player 2 Win's")
    else:
        print("Player 1 Win's")


if __name__ == "__main__":
    mn = int(input("Enter a minimum number\n"))
    mx = int(input("Enter a maximum number\n"))
    ran = gen_randon_num(mn, mx)
    player1 = guess_num("Player 1", ran)
    ran2 = gen_randon_num(mn, mx)
    player2 = guess_num("Player 2", ran2)

    winner(player1, player2)
