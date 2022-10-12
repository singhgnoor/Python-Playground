""" This is a Python file that calculates the investment made on monthly basis and generates outputs """
from time import sleep
import os
import csv


class Investor:
    __years = None
    __monthly_invest = None
    __months = None
    __rate_of_interest = None
    __yearly_increase = 0
    __return_investment = None
    __csv_data = []
    __csv_header = ["Year", "Months", "Invested Amount", "Actual Amount"]

    def set_yearly_increase(self, _yearly_increase): self.__yearly_increase = _yearly_increase

    def monthly_calculator(self, monthly_investemnt, months, rate_of_interest, basic_amount=0, write_csv=False):
        if monthly_investemnt is None or months is None or rate_of_interest is None:
            print("Required Values Not given")
            return

        csv_data = []

        initial_amount = monthly_investemnt + basic_amount

        months -= 1
        self.__years = int((months - (months % 12)) / 12)
        amount = initial_amount
        csv_data.append([1, 0, f"{initial_amount :,.2f}", f"{amount :,.2f}"])
        for i in range(int(self.__years)):
            for j in range(12):
                amount = (amount * rate_of_interest * (1 / 12) / 100) + amount

                # for write_csv function
                csv_data.append([i+1, j+1, f"{(((i * 12) + (j + 1)) * monthly_investemnt) + basic_amount :,.2f}", f"{amount :,.2f}"])
                amount += monthly_investemnt
            monthly_investemnt += self.__yearly_increase

        if (months % 12) != 0:
            for i in range(months % 12):
                amount = (amount * rate_of_interest * (1 / 12) / 100) + amount
                amount += monthly_investemnt

        if write_csv: self.__csv_data = csv_data
        return amount

    def __investment_by_factor(self, investment_amount, time, rate, factor):
        amount = (investment_amount * rate * (factor/12) / 100) + investment_amount

        for i in range(time - 1):
            amount = (amount * rate * (factor/12) / 100) + amount
            amount += investment_amount

        self.__return_investment = amount
        return self.__return_investment

    def yearly_investment(self, yearly_investemnt, years, rate_of_interest):
        return self.__investment_by_factor(yearly_investemnt, years, rate_of_interest, 12)

    def half_yearly_investment(self, yearly_investemnt, years, rate_of_interest):
        return self.__investment_by_factor(yearly_investemnt, years, rate_of_interest, 6)

    def write_csv(self, file_name):
        if self.__csv_data == [] or self.__csv_data is None: return False
        with open(f"D:\\Python\\Playground\\Investor\\investment_sheets\\{file_name}", "w",  encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.__csv_header)
            writer.writerows(self.__csv_data)
        return True


if __name__ == '__main__':
    investor = Investor()
    principal_amount, basic_principal_amount, months_, rate_, yearly_increase, = [None for i in range(5)]

    try:
        principal_amount = int(input("Amount for monthly Investment : "))
        basic_principal_amount = int(input("Any Amount that is Pre-Invested (if not pls give 0) : "))
        months_ = int(input("Months for investment : "))
        rate_ = float(input("Rate of interest : "))
        yearly_increase = int(input("Yearly increase : "))
    except ValueError:
        print("Invalid value given for variables. ")
        print("Restarting", end="")
        for i in range(10):
            print(".", end="")
            sleep(1 - i*.1)
        print("\n\n\n")
        os.system(f"python -u {__file__}")
        exit()

    your_investment = (months_ * principal_amount) + basic_principal_amount

    return_investment = investor.monthly_calculator(principal_amount, months_, rate_, basic_amount=basic_principal_amount, write_csv=True)

    # Setting Yearly increase
    investor.set_yearly_increase(yearly_increase)
    return_investment_new = investor.monthly_calculator(principal_amount, months_, rate_, basic_amount=basic_principal_amount)

    print(f"\n\nYour Investment : {your_investment :,.2f}\nReturn you get : {return_investment :,.2f}")

    increased_investment = 0
    for i in range(int((months_ - (months_ % 12)) / 12) - 1): increased_investment += yearly_increase * 12

    if (months_ % 12) != 0: increased_investment += (months_ % 12) * yearly_increase

    print(f"\n\nAnd now if we increase the investment by {yearly_increase} each year\nYour Investment : {(your_investment + increased_investment) :,.2f}\nReturn you get : {return_investment_new :,.2f}")
    print(f"Time taken : {int((months_ - (months_ % 12)) / 12)} Year(s) and {months_ % 12} Month(s)")

    investor.write_csv("myInvestor.csv")
