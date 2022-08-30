import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_MAP_API_KEY")

params = {
    "lat": "60.25",
    "lon": "24.6667",
    "exclude": "minutely,current,daily",
    "APPID": api_key
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params)
response.raise_for_status()

data = response.json()

will_rain = False
for weather in data["hourly"][:12]:
    if int(weather["weather"][0]["id"]) < 700:
        will_rain = True
        break

if will_rain:
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an ☔️",
                                     from_=os.getenv("FROM_PHONE_NUMBER"), to=os.getenv("TO_PHONE_NUMBER"))
    print(message.status)
