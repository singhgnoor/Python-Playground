# Started at 16:00 22-03-2021
print("Welcome to Python Mensuration Solver")
print("We will solve Problems of Mensuration for You")

print("What Kind of object Do you Have?")
print("Press following Button for the following Object")
print("Trapizium               : 1")
print("Circle                  : 2")
print("Cube                    : 3")
print("Cuboid                  : 4")
print("Right Circular Cylender : 5")
ObjType = input("")

unit = input("What is the Unit of the Object : ")

if ObjType == "1":
    print("So you have a Trapizium.")
    print("Please Fill The follwing")
    a = float(input("What is First parallel side     : "))
    b = float(input("What is Second parallel side    : "))
    h = float(input("What is the height of Trapizium : "))
    ans = (((a + b) * (1/2)) * h)
    print(f"Area of Your Trapizium is {ans}{unit}²")

elif ObjType == "2":
    print("So you have a Circle.")
    print("What you want to find from the following")
    print("Area           : 1 ")
    print("Circumferance  : 2 ")
    OutType = input("")
    r = float(input("What is the Diameter of the Cicrle  : "))
    if OutType == "1":
        area = ((22/7) * r * r)
        print(f"Area of Circle is {area}{unit}²")

    elif OutType == "2":
        circumferance = (2 * (22/7) * r)
        print(f"Circumferance of Circle is {circumferance}{unit}")

    else:
        print("Invalid Choice")

elif ObjType == "3":
    print("So you have a Cube.")
    print("What you want to find from the following")
    print("Volume         : 1 ")
    print("Surface Area   : 2 ")
    OutType = input("")
    side = float(input("What is the Side of the Cube  : "))
    if OutType == "1":
        volume = side * side * side
        print(f"Volume of Cube is {volume}{unit}")

    elif OutType == "2":
        Surface_Area = 6 * side * side
        print(f"Surface Area of Cube is {Surface_Area}{unit}²")

    else:
        print("Invalid Choice")

elif ObjType == "4":
    print("So you have a Cuboid.")
    print("What you want to find from the following")
    print("Volume         : 1 ")
    print("Surface Area   : 2 ")
    OutType = input("")
    lenght = float(input("What is the Lenght of the Cube   : "))
    breagth = float(input("What is the Breagth of the Cube  : "))
    height = float(input("What is the Height of the Cube   : "))
    if OutType == "1":
        volume = lenght * breagth * height
        print(f"Volume of Cuboid is {volume}{unit}")

    elif OutType == "2":
        Surface_Area = 2 * (lenght*breagth + breagth*height + height*lenght)
        print(f"Surface Area of Cuboid is {Surface_Area}{unit}²")

    else:
        print("Invalid Choice")

elif ObjType == "5":
    print("So you have a Right Circular Cylender.")
    print("What you want to find from the following")

else:
    print("Invalid Choice")
