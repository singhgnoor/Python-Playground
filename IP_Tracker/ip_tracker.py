""" This is a file that takes in the client ip address and spits out the most possible location of that ip"""
import requests
from datetime import datetime, date
import time


class IpTracker:
    def __init__(self):
        self.ip = None
        self.brief = None

    def getSelfIp(self):
        print("Getting Device ip.")
        self.ip = requests.get('https://api64.ipify.org?format=json').json()["ip"]
        return self.ip

    def setIp(self, ipAdr):
        self.ip = ipAdr

    def getIpInformation(self, ipAdr=None):
        if ipAdr is None and self.ip is None:
            print("Tracking client device ip Address!")
            ipAdr = self.getSelfIp()
        print(f"\nTracking {ipAdr}...")
        response = requests.get(f"https://ipapi.co/{ipAdr}/json/").json()
        # Formatting Information
        self.brief = self.formatInformation(info=response, getInfo=False)
        # Logging the scrapped information
        self.logIp(brief=self.brief)
        return response

    def formatInformation(self, info=None, getInfo=True):
        if info is None and getInfo:
            info = self.getIpInformation(ipAdr=self.ip)

        if info is None: return None

        brief = f"IP Address : {info['ip']}\nCity : {info['city']}\nRegion(State) : {info['region']}\nCountry : {info['country_name']}\nPostal Code : {info['postal']}\nService Provider : {info['org']}\nLatitude, Longitude : {info['latitude']},{info['longitude']}\nGoogle Maps link : https://www.google.com/maps/search/{info['latitude']},{info['longitude']}"

        return brief

    def logIp(self, brief=None):
        if brief is None and self.brief is None:
            print("Unable to write a log.")
            return

        if brief is None:
            brief = self.brief

        with open(f"tracked_ip\\IP Tracker {str(datetime.now()).replace(':', '').replace(' ', '-')}", "w") as file:
            toWrite = f"Time : {time.strftime('%H:%M:%S', time.localtime())}\nDate : {date.today()}\n\n{brief}"
            file.write(toWrite)
        return


if __name__ == '__main__':
    print("Welcome to the IP Tracker!")

    ipTracker = IpTracker()

    ip_adr = input("Any Particular ip you want to track, if not hit enter : ")
    if ip_adr.replace(" ", "") == "":
        ip_adr = None
        information = ipTracker.getIpInformation()
    else:
        information = ipTracker.getIpInformation(ipAdr=ip_adr)

    print(ipTracker.formatInformation(info=information))
