from time import sleep
from os import startfile
print("Welcome To The Compound Interest Calculator!")
sleep(2)
print("Please Enter The Following Details:-")
p = input("Principal (₹): ")
r = input("Rate of Interest(%) : ")
t = input("Time In Year : ")
# if '%' in r:
#     r.replace('%', '')

try:
    p = float(p)
except:
    print("Please Give Inter (number) parameter")
    p = ""      
    p = input("Principal (₹): ")

try:
    r = float(r)
except:
    print("Please Give Inter (number) parameter")
    r = ""                 
    r = input("Rate of Interest(%) : ")

try:
    t = float(t)
except:
    print("Please Give Inter (number) parameter")
    t = ""
    t = input("Time In Year : ")

if int(t) > 100:
    print('The time Given Was More Than 100 Years so Cannot Calculate The Sum!')
    exit()

try:
    print(f"\nCalculating The Given Arguments")
    sleep(1)
    if float(t) < 1:
        si = (float(p)*float(r)*float(t))/100
        p += si
    else:
        for y in range(int(t)):
            si = (float(p)*float(r)*1)/100
            p += si
            print(f"Year {round( y + 1 , 2 )} = {round( p , 2 )}")
            if t > 50:
                sleep(0.01)
            else:
                sleep(0.1)
    print(f"\nCompound Interest = ₹ {round(p, 2)}")
    print("Your Monthly Payment will Be : ₹", round(p/(float(t)*12), 2))
except Exception as e:
    print(e)
    print("Invalid Parameters")
    exit()
print("\nThank You For Using Our Servise\n")
con = input("\nTo Exit Press 1\n")
if con == "1":
    exit()