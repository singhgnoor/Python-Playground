from time import sleep

print(
    "Welcome To The Smart Statics And Probability Calculator !. Here You Can Solve Very Difficult And Lengthy Sum of The Static")

# Taking Required Values
# Taking Number of Input
numOfItems = input("Number of Items you Have : ")
# Error Handling of it 
try:
    numOfItems = int(numOfItems)
except:
    try:
        print("Please Give a Integer (number) Parameter")
        numOfItems = int(input("Number of Items you Have : "))
    except:
        print("The Para meter Given Was not Integer So Cannot Process it")
        sleep(5)
        exit()

items = []
print("Give the Value for Each Place")
# Value for Eac Place
for n in range(numOfItems):
    whatToTake = input(f"\nValue at {n + 1} : ")
    # Error Handling of it 
    try:
        whatToTake = float(whatToTake)
    except:
        try:
            print("Please Give a Number Parameter")
            whatToTake = float(input(f"Value at {n + 1} : "))
        except:
            print("The Para meter Given Was not Integer So the Value is = 0")
            whatToTake = 0.0

    items.append(whatToTake)

print("\n")
ClassSize = input("Class Size : ")

# Error Handling of it 
try:
    ClassSize = float(ClassSize)
except:
    try:
        print("Please Give a Number Parameter")
        ClassSize = float(input("Class Size : "))
    except:
        print("The Para meter Given Was not Integer So Taking Class Size = 5")

# Taking Highest Value
high = input("What is the Highest Value  : ")

# Error Handling of it 
try:
    high = float(high)
except:
    try:
        print("Please Give a Number Parameter")
        high = float(input("What is the Highest Value  : "))
    except:
        print("The Para meter Given Was not Integer So Taking Class Size = 5")

# Taking Lowest Value
low = input("What is the Lowest Value  : ")

# Error Handling of it 
try:
    low = float(low)
except:
    try:
        print("Please Give a Number Parameter")
        low = float(input("What is the Lowest Value  : "))
    except:
        print("The Para meter Given Was not Integer So Taking Class Size = 5")

# Required Values Taken

print("Calculating Given Values")
sleep(2)

HighCl = int(high) % int(ClassSize)
LowCl = int(low) % int(ClassSize)

HighClass = high + HighCl + ClassSize
LowClass = low - LowCl - ClassSize

TallyM = {}
print("\n")

print("Printing The Values")
sleep(.9)
for i in range(int(((HighClass - LowClass) / ClassSize) + ClassSize)):
    for it in items:
        if (i * ClassSize) <= it < ((i + 1) * ClassSize):
            if f"{i * ClassSize} - {(i + 1) * ClassSize}" in TallyM:
                upp = TallyM.get(f"{i * ClassSize} - {(i + 1) * ClassSize}")
                upp = upp + 1
                print(f"{it} in {i * ClassSize} - {(i + 1) * ClassSize}")
                TallyM.update({f"{i * ClassSize} - {(i + 1) * ClassSize}": upp})
            else:
                print(f"{it} in {i * ClassSize} - {(i + 1) * ClassSize}")
                TallyM.update({f"{i * ClassSize} - {(i + 1) * ClassSize}": 1})

print("\n")
print("All The Values Are Calculated Giving the Result")
sleep(1)
for k, val in TallyM.items():
    print(f"{k} : {val}")

print("Thank You For Using Our Service! Visit Again.")
sleep(10)
input("To exit Hit Enter  ")
