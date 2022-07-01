from random import randint
def funnny_name (name, n):
    fun = []
    fun1 = []
    for i in range(n):
        a = randint(0, n)
        b = randint(0, n)
        fun.append(a)
        fun1.append(b)
    fun2 = zip(fun, fun1)
    return fun2

n_fri = int(input("Enter number of friends\n"))

names = []
for i in range(n_fri):
    a = input(f"Enter name of {i} friend\n")
    names.append(a)
print(dict(funnny_name(names, n_fri)))


