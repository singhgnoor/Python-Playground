from time import sleep
print("Welcome To The Simple Interest Calculator!")
sleep(2)
print("Please Enter The Following Details:-")
p = input("Principal : ")
r = input("Rate of Interest(%) : ")
t = input("Time In Year : ")
# if '%' in rate_of_interest:
#     rate_of_interest.replace('%', '',1)

try:
    p = float(p)
except:
    print("Please Give Inter (number) parameter")
    p = ""      
    p = input("Principal : ")

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


try:
    print(f"\nCalculating The Given Arguments")
    sleep(1)
    si = (float(p)*float(r)*float(t))/100
    print(f"\nSimple Interest = {si}")
    print(f"Amount  = {si+p}")
except Exception as e:
    print(e)
    print("Invalid Parameters")
    exit
