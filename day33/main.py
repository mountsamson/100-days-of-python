import requests
from datetime import datetime

MY_LAT =  37.8136
MY_LONG = 144.9631

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']["longitude"]
# latitude = data['iss_position']["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get (url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
    
    
time_now =datetime.now()

print(time_now.hour)

