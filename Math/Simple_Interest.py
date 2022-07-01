from time import sleep


def convert_to_float(inp, msg_to_show):
    """ This function takes str input and tries to convert it to float"""
    try: return float(inp)
    except ValueError: convert_to_float(input(msg_to_show), msg_to_show=msg_to_show)
    except Exception: raise Exception


def simple_interest_calculator(principal, rate_of_interest, time_period):
    return (principal * rate_of_interest * time_period) / 100


if __name__ == '__main__':
    print("Welcome To The Simple Interest Calculator!")
    sleep(1)
    print("Please Enter The Following Details:-")

    principle_ = convert_to_float(input("Principal (₹) : "), "Please Give Inter (number) parameter for Principal(₹) : ")
    rate_ = convert_to_float(input("Rate of Interest (%) : "), "Please Give Inter (number) parameter for Rate of Interest (%) : ")
    time_ = convert_to_float(input("Time (year) : "), "Please Give Inter (number) parameter for Time (year) : ")

    print(f"\nCalculating The Given Arguments")
    sleep(1)
    results = simple_interest_calculator(principal=principle_, rate_of_interest=rate_, time_period=time_)

    print(f"Simple Interest : ₹{results}")
