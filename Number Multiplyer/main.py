# Class 11 Final IP Practice 2021

import os

os.chdir("../")
print("Printing .git Folders")
for filePath, folders, fileName in os.walk(os.getcwd()):
    if filePath.endswith(".git"):
        print(filePath)
