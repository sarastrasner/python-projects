import requests
from twilio.rest import Client
import os

parameters = {
    "lat": 39.739235,
    "lon": -104.990250,
    "exclude": "current,minutely,daily",
    "appid": "3bb4547d22ba25d1c922274a905ae485"
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
account_sid = os.environ.get('OWM_KEY')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
my_number = os.environ.get('MY_NUMBER')
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Bring an ☂️.",
        from_='+16789819663',
        to=my_number
    )

    print(message.status)


