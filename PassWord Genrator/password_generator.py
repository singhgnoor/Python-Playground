from functions import PassWordGenrator, PassWordSaver, PassTypeGetter, PassLenGetter
import subprocess


def main(passType, passLen, passPurpose):
    PassWord = PassWordGenrator(passType, passLen)

    print("So here is what i got for you")
    print(f"PassWord Type    : {passType}")
    print(f"PassWord Length  : {passLen}")
    print(f"PassWord Purpose : {passPurpose}")
    print(f"PassWord         : {PassWord}\n\n")
    con = input("Like this if not press 1 or if you like this one press 2 to continue\n")
    if con == "1":
        print("Re-Generating your Password")
        main(passType, passLen, passPurpose)
    
    else:
        PassWordSaver(passPurpose, PassWord)

    subprocess.check_call(f"echo {PassWord} |clip", shell=True)
    print("The Password has been copied to your clipboard.")


if __name__ == '__main__':
    print("Welcome!! to PassWord Generator")
    print("We will Generate Random PassWord for you and Save item for Later")

    PassType = PassTypeGetter()
    PassLen = PassLenGetter()
    PassPurpose = input("What is the Purpose of the PassWord?\n")

    main(PassType, PassLen, PassPurpose)

    print("ThankYou For using our services. Use Again")
