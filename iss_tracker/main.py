import requests
from datetime import datetime
import smtplib
import time
import os


MY_LAT = 39.739235
MY_LONG = -104.990250
MY_EMAIL = os.environ.get("EMAIL")
MY_PASSWORD = os.environ.get("PASSWORD")


# TODO: Create fn that returns true or false if your position is within +5 or -5 degrees of the ISS position.
def check_iss_proximity():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    """Returns true if the ISS is close by, false if not"""
    if MY_LONG-5 <= iss_longitude <= MY_LONG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        print("The ISS is close by!")
        return True
    else:
        print("The ISS is NOT close by!")
        return False


def check_nighttime():
    """Returns true if it's nighttime, false if not"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = int(str(datetime.now()).split(' ')[1].split(":")[0])
    # print(f"Sunrise: {sunrise}")
    # print(f"Sunset: {sunset}")
    # print(f"Current hour: {time_now}")
    if time_now >= sunset or time_now <= sunrise:
        print("It's dark out!")
        return True
    else:
        return False


while True:
    time.sleep(60)
    if check_nighttime() and check_iss_proximity():
        print("Sending an email")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Go outside!\n\nThe ISS is nearby!")

# TODO: If the ISS is close to my current position
# TODO: and it is currently dark
# TODO: Then send me an email to tell me to look up.
# TODO: run the code every 60 seconds.
