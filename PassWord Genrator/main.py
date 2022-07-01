from functions import PassWordGenrator, PassWordSaver, PassTypeGetter, PassLenGetter

print("Welcome!! to PassWord Genrator")
print("We will Genrate Random PassWord for you and Save it for Later")


def main(PassType, PassLen, PassPurpose):
    PassWord = PassWordGenrator(PassType, PassLen)

    print("So here is what i got for you")
    print(f"PassWord Type    : {PassType}")
    print(f"PassWord Length  : {PassLen}")
    print(f"PassWord Purpose : {PassPurpose}")
    print(f"PassWord         : {PassWord}\n\n")
    con = input("Like this if not press 1 or if you like this one press 2 to continue\n")
    if con == "1":
        print("Re-Genrating your Password")
        main(PassType, PassLen, PassPurpose)
    
    else:
        PassWordSaver(PassPurpose, PassWord)

PassType = PassTypeGetter()
PassLen = PassLenGetter()
PassPurpose = input("What is the Purpose of the PassWord?\n")

main(PassType, PassLen, PassPurpose)

print("ThankYou For using our servies. Use Again")