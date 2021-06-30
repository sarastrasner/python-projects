import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']["longitude"]
# latitude = data['iss_position']["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

MY_LAT = 39.739235
MY_LONG = -104.990250

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=F"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()['results']
sunrise = data['sunrise'].split('T')[1].split(':')[0]
sunset = data['sunset']


print(f"Sunrise hour: {sunrise}")
time_now = dt.datetime.now().hour
print(f"Current hour: {time_now}")
