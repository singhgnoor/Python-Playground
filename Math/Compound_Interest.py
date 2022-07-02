from time import sleep


def convert_to_float(inp, msg_to_show):
    """ This function takes str input and tries to convert item to float"""
    try: return float(inp)
    except ValueError: return convert_to_float(input(msg_to_show), msg_to_show=msg_to_show)
    except Exception: raise Exception


def compound_interest_calculator(principal_, rate, time):
    """ This function takes p, r, t as input and return compound interest """
    year_dict = []
    if float(time_) < 1:
        simple_interest = (principal_ * rate * time) / 100
        principal_ += simple_interest
    else:
        for year_ in range(int(time)):
            simple_interest = (principal_ * rate * 1) / 100
            principal_ = simple_interest + principal_
            year_dict.append(f"Year {round(year_ + 1 , 2 )} : ₹{round( principal_ , 2 )}")
    return year_dict, principal_


if __name__ == '__main__':
    print("Welcome To The Compound Interest Calculator!")
    sleep(2)

    # Taking input
    principal = convert_to_float(input("Principal (₹): "), "Please Give Inter (number) parameter for Principal Amount (₹) : ")
    rate_of_interest = convert_to_float(input("Rate of Interest(%) : "), "Please Give Inter (number) parameter for Rate of Interest (%) : ")
    time_ = convert_to_float(input("Time In Year : "), "Please Give Inter (number) parameter for Time (Year) : ")

    years, result = compound_interest_calculator(principal_=principal, rate=rate_of_interest, time=time_)

    for year in years:
        print(year)
        sleep(0.1)

    print(f"\n\nTotal Amount to be paid : ₹{round(result, 2)}")

    print(f"\n\nYour Monthly Payment will Be : ₹{round((result / time_ * 12), 2)}, for {time_ * 12} months")
