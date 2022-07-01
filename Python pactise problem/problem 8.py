from random import randint
# wrong = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
def rohanMultiplication(n):
    a = randint(2,8)
    multi = []
    # print(a)
    for i in range(10):
        if i != 5:
            multi.append((i+1)*n)
        else:
            multi.append(((i+1)*n)+2)
    return multi

def isCorrect(table, number):
    a = None
    for items in table:
        if items % number != 0:
            a = items 
        else:
            pass
    return a
            
if __name__ == "__main__":
    x = randint(1,10)
    print(f"The output of rohan multiplicaton is {rohanMultiplication(x)}")
    print(f"Wrong number is {isCorrect(rohanMultiplication(x), x)}")
    if isCorrect(rohanMultiplication(x), x) == None:
        print("Rohan is coorect")
    else:
        print("Rohan is froud")