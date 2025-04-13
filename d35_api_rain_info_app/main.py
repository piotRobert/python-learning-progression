import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
OWM_Endpoint = os.getenv("OWM_ENDPOINT")
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat": 52.357460,
    "lon": 16.516809,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hourd_data in weather_data["list"]:
    if hourd_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella",
    from_="{phone_number}",
    to="{phone_number}",
    )
    print(message.status)