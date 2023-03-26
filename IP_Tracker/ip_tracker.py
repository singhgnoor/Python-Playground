""" This is an file that takes in the client ip address and spits out the most possible location of that ip"""
import pygeoip


def track_ip(ip_address) -> dict: return pygeoip.GeoIP("GeoLiteCity.dat").record_by_addr(ip_address)


def get_formatted_track_ip(ip_address) -> dict:
    data = track_ip(ip_address)
    new_data = {}

    for key_, val in data.items():
        if key_ == "latitude" or key_ == "longitude":
            new_data[key_] = round(val, 4)
        else:
            new_data[key_] = val

    brief_info = f"IP Address : {ip_address}\nCountry : {new_data['country_name']}\nCity : {new_data['city']}\nTime Zone : {new_data['time_zone']}\nLatitude, Longitude : {new_data['latitude']}, {new_data['longitude']}"
    new_data["brief"] = brief_info
    return new_data


if __name__ == '__main__':
    print("Welcome to the Ip Tracker")
    ip_addr = input("Which IP Address do you want to find? - ")
    print(get_formatted_track_ip(ip_addr)["brief"])

