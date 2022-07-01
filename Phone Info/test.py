from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier

number = "+918968152575"
# this will prase the number into Country Code and number
new = phonenumbers.parse(number , "CH")
print(new)

# this will print region of the phone number
print(geocoder.description_for_number(new, "en"))

# this will provide the company of wich the number is
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))