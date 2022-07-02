import pickle
import random
import os

def PassWordSaver(purpose, passWord):
    op = input("You want to save your PassWord Yes or No\n")
    if op.lower() == "yes":
        if not os.path.exists("SavedPassWords.pkl"):
            f = open("SavedPassWords.pkl", 'wb')
            SavePass = f"{purpose}:{passWord}"
            passlist = [SavePass]
            print(f"Dumping {passlist} into SavedPassWords.pkl")
            pickle.dump(passlist, f)
            f.close()
        
        elif os.path.exists("SavedPassWords.pkl"):
            f = open("SavedPassWords.pkl", "rb")
            SavePass = f"{purpose}:{passWord}"
            passlist = pickle.load(f)
            f.close()
            passlist.append(SavePass)

            f = open("SavedPassWords.pkl", "wb")
            pickle.dump(passlist, f)
            f.close()
        print("Your Paassword is Saved You can revive Password Anytime!")
        return

    else:
        con = input("Warning! if you do not save your passWord we would not Help you to remember your passWord (to save password press 1 else press 2)\n")
        if con == "1":
            PassWordSaver(purpose, passWord)
        else:
            print("Password not saved")
            return

def PassWordGenrator(type, len):
    passWord = ""
    charStr = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    numStr = "1234567890"
    spStr = """!@#$%^&*()_+"<>?-=[];',./"""

    if type == "mixed":
        Option = "123"
        for i in range(len):
            if str(random.choice(Option)) == "1":
                passWord += random.choice(charStr)
            
            if str(random.choice(Option)) == "2":
                passWord += random.choice(numStr)
            
            if str(random.choice(Option)) == "3":
                passWord += random.choice(spStr)
    
    elif type == "char":
        for i in range(len):
            passWord += random.choice(charStr)
    
    elif type == "number":
        for i in range(len):
            passWord += random.choice(numStr)
    
    return passWord

def PassTypeGetter():
    passType = input("What kind of PassWord you Want? Number, Char or Mixed. (just copy and paste item)\n")

    if passType.lower() == "number":
        return "number"
    
    elif passType.lower() == "char":
        return "char"
    
    elif passType.lower() == "mixed":
        return "mixed"
    
    else:
        ty = input("Invalid Type To Select Again Press 1 and Hit Enter else Press 2\n")
        if ty == "1":
            PassTypeGetter()
        else:
            print("ThankYou For using our servies. Use Again")
            exit()

def PassLenGetter():
    len = input("What will be the Length of Your Password\n")

    try:
        len = int(len)
        return len

    except:
        ty = input("It Should be a Number! To type again press 1 and hit enter esle press 2\n")
        if ty == "1":
            PassLenGetter()
        else:
            print("ThankYou For Using our service!")