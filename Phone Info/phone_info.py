import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from time import sleep

print("Welcome to Phone Tracker. We will Track your phone.")
sleep(2)
print("Please enter your phone number Which you want to track")
number = input("Example +918596456981 : ")

try: 
    # this will prase the number into Country Code and number
    new = phonenumbers.parse(number , "CH")
    print(new)

    # this will print region of the phone number
    print(geocoder.description_for_number(new, "en"))

    # this will provide the company of wich the number is
    service_provider = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_provider, "en"))

except Exception as error:
    print(f"Unable to get info due to {error}")