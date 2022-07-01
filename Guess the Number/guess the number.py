from random import randint

# a = randint(0, 10)
# b = randint(0, 10)

a = 2
b = 5

print("A/B = ", a/b)
print("A*B = ", a*b)
print("A+B = ", a+b)
print("A-B = ", a-b)

guessA = input("Now Pls Guess A : ")
guessB = input("Now Pls Guess B : ")

if a != guessA or b != guessB:
    print(f"Wrong Guess!!\n A = {a} and B = {b}")

else:
    print("Whoa!! Great Your ans is Correct")