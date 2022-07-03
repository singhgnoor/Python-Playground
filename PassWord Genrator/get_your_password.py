import pickle
import os 

if not os.path.exists("SavedPassWords.pkl"):
    print("You do not have any PassWord!")
    exit()

if os.path.exists("SavedPassWords.pkl"): 
    passW = input("Please Enter your Laptop's PassWord in order to see Your PassWord List\n")
    if passW == "15625":
        f = open("SavedPassWords.pkl", "rb")
        passlist = pickle.load(f)
        f.close()
        for i in passlist:
            i = i.split(":")
            print(f"PurPose : {i[0]}, PassWord : {i[1]}")