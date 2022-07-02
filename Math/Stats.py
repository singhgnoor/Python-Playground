from time import sleep


def convert_to_int(inp, msg_to_show):
    """ This function takes str input and tries to convert item to int"""
    try: return int(inp)
    except ValueError: return convert_to_int(input(msg_to_show), msg_to_show=msg_to_show)
    except Exception: raise Exception


def convert_to_float(inp, msg_to_show):
    """ This function takes str input and tries to convert item to float"""
    try: return float(inp)
    except ValueError: return convert_to_float(input(msg_to_show), msg_to_show=msg_to_show)
    except Exception: raise Exception


def Tally_Calculator(items_list, class_size):
    """ This function distributes items in classes of given sizes"""
    TallyM = {}
    print_list = []

    # Highest and Lowest Value's
    high = max(items_list)
    low = min(items_list)

    # Getting range for running the loop
    HighClass = (high - (high % class_size)) + class_size
    LowClass = (low - (low % class_size))

    for i in range(int(str(low/class_size).split(".")[0]), int((HighClass - LowClass) / class_size) + 1):
        for item in items_list:
            if (i * class_size) <= item < ((i + 1) * class_size):
                if f"{i * class_size} - {(i + 1) * class_size}" in TallyM:
                    upp = TallyM.get(f"{i * class_size} - {(i + 1) * class_size}")
                    upp = upp + 1
                    print_list.append(f"{item} in {i * class_size} - {(i + 1) * class_size}")
                    TallyM.update({f"{i * class_size} - {(i + 1) * class_size}": upp})
                else:
                    print_list.append(f"{item} in {i * class_size} - {(i + 1) * class_size}")
                    TallyM.update({f"{i * class_size} - {(i + 1) * class_size}": 1})
    return TallyM, print_list


if __name__ == '__main__':
    # Taking Required Values
    # Taking Number of Input
    numOfItems = convert_to_int(input("Number of Items you Have : "), msg_to_show="Please Give a Integer (number) Parameter")

    items = []
    print("Give the Value for Each Place")
    # Value for Each Place
    for n in range(numOfItems):
        whatToTake = convert_to_float(input(f"\nValue at {n + 1} : "), msg_to_show=f"Please Give a Number (float) Parameter for - Value at {n + 1} : ")
        items.append(whatToTake)

    classSize = convert_to_float(input("\n\nClass Size : "), msg_to_show="Please Give a Number(Integer) Parameter for classSize")

    if classSize == 0.0:  # This can give zero division error
        print("Class Size can not be zero!")
        exit()

    # Required Values Taken

    print("Calculating Given Values\n")
    sleep(2)

    result, list_to_print = Tally_Calculator(items_list=items, class_size=classSize)

    print("Printing The Values")
    sleep(.9)

    for print_item in list_to_print:
        print(print_item)
        sleep(0.1)

    print("\nAll The Values Are Calculated Giving the Result")
    sleep(1)
    for key, val in result.items():
        print(f"{key} : {val}")

    print("Thank You For Using Our Service! Visit Again.")
    sleep(10)
    input("To exit Hit Enter  ")
