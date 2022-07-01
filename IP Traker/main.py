import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr("157.245.110.62")

for key, value in res.items():
    print(f"{key}   :  {value}")
