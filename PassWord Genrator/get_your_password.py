import pickle
import os 

if not os.path.exists("SavedPassWords.pkl"):
    print("You do not have any PassWord!")
    exit()

if os.path.exists("SavedPassWords.pkl"): 
    passW = input("Please Enter your Laptop's PassWord in order to see Your PassWord List\n")
    with open("SavedPassWords.pkl", "rb") as f:
        passList = pickle.load(f)
        for i in passList:
            i = i.split(":")
            print(f"PurPose : {i[0]}, PassWord : {i[1]}")