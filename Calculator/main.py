print("Welcome!!!")
statemnt = input("What is Your Calculation (eg 12+13)\n")

if "+" in statemnt:
    statemnt = statemnt.split("+")
    ans = 0
    for i in statemnt:
        ans = ans+float(i)

if "-" in statemnt:
    statemnt = statemnt.split("-")
    ans = 0
    for i in statemnt:
        ans = ans-float(i)

if "*" in statemnt:
    statemnt = statemnt.split("*")
    ans = 1
    for i in statemnt:
        ans = ans*float(i)

if "/" in statemnt:
    statemnt = statemnt.split("/")
    ans = 1
    for i in statemnt:
        ans = ans/float(i)

print(ans)