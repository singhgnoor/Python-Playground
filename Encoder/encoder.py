"""This file encodes and decodes strings and integers"""

from time import sleep
import hashlib, base64

class Encoder:
    str_to_encode = None

    def __init__(self, str_to_encode):
        self.str_to_encode = str_to_encode

    def sha_256(self, str_to_encode=str_to_encode):
        return hashlib.sha256(str_to_encode.encode('utf-8'))

    def sha_512(self, str_to_encode=str_to_encode):
        return hashlib.sha512(str_to_encode.encode('utf-8'))

    def sha_1(self, str_to_encode=str_to_encode):
        return hashlib.sha1(str_to_encode.encode('utf-8'))

    def base_64(self, str_to_encode=str_to_encode):
        return base64.b64encode(str_to_encode.encode('utf-8')).decode('utf-8')

if __name__ == '__main__':
    print("Welcome to Encoder! Please chose type of encoding you want.")

    strToEncode = input("What you do want to encode :")
    if strToEncode == "" or strToEncode == None:
        print("Nothing given to Encode.")
        sleep(1)
        exit()

    enType = input("For custom encoding press '1'\nFor pre-built encoding press '2'")

    if enType == "1":
        print("Under construction")
    elif enType == "2":
        preBuiltType = input("Options available: \n1. SHA-1\n2. SHA-256\n3. SHA-512\n4. Base-64")

        if preBuiltType == "1":
            print("SHA-1")
        elif preBuiltType == "2":
            print("SHA-256")
        elif preBuiltType == "9":
            print("SHA-512")
        elif preBuiltType == "1":
            print("Base-64")
        else:
            print("Not a valid option")
            sleep(1)
            exit()

        primnt()       


    else:
        print("Not a Valid option")
        sleep(1)
        exit()


