print("Welcome!!!")
statement = input("What is Your Calculation (eg 12+13)\n")

ans = None

if "+" in statement:
    statement = statement.split("+")
    ans = 0
    for i in statement:
        ans = ans+float(i)

if "-" in statement:
    statement = statement.split("-")
    ans = 0
    for i in statement:
        ans = ans-float(i)

if "*" in statement:
    statement = statement.split("*")
    ans = 1
    for i in statement:
        ans = ans*float(i)

if "/" in statement:
    statement = statement.split("/")
    ans = 1
    for i in statement:
        ans = ans/float(i)

print(ans)
