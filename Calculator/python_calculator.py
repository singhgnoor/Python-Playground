""" Simple python calculator in which the Statement(string) is converted into a float and applied corresponding operator """


class Calculator:
    __statement = None

    def __init__(self, statement): self.__statement = statement

    def decide_and_calculate(self):
        if "+" in self.__statement: return self.addition()
        elif "-" in self.__statement: return self.subtraction()
        elif "*" in self.__statement: return self.multiplication()
        elif "/" in self.__statement: return self.division()
        else: print("Operator not included")

    def addition(self, statement=__statement):
        if statement is None: statement = self.__statement
        statement = statement.split("+")
        ans = 0
        try:
            for i in statement: ans = ans + float(i)
        except TypeError: print("Cannot add string to integer.")
        return ans

    def subtraction(self, statement=__statement):
        if statement is None: statement = self.__statement
        statement = statement.split("-")
        ans = float(statement[0])
        try:
            for i in statement[1::]: ans = ans - float(i)
        except TypeError:
            print("Cannot subtract string from an integer.")
        return ans

    def multiplication(self, statement=__statement):
        if statement is None: statement = self.__statement
        statement = statement.split("*")
        ans = 1
        try:
            for i in statement: ans = ans * float(i)
        except TypeError:
            print("Cannot multiply string and an integer.")
        return ans

    def division(self, statement=__statement):
        if statement is None: statement = self.__statement
        statement = statement.split("/")
        ans = float(statement[0])
        try:
            for i in statement[1::]:  ans = ans / float(i)
        except TypeError:
            print("Cannot divide string and an integer.")
        except ZeroDivisionError:
            print("Cannot divide by zero(0).")
        return ans


if __name__ == '__main__':
    print("Welcome to the Calculator!")
    st_ment = input("Enter the statement to operate on (eg - 13+12) : ")
    print(Calculator(st_ment).decide_and_calculate())
    print("Thank You!")
