import requests
from twilio.rest import Client


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api = "1428db25cd7fb7f81ed9b78c81f34c2f"
account_sid = "AC6a692a27ab5905d9f1b42e3e58154c00"
auth_token = "021efbcbde02507f0d90be9a92ae92e1"

weather_para = {
    "lat": 24.272070,
    "lon": 120.703033,
    "appid": api,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=weather_para)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

wil_rain = False
for hourly_data in weather_slice:
    condition = hourly_data["weather"][0]["id"]
    if int(condition) < 700:
        wil_rain = True

if wil_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is rainy today taken an umbrella",
            from_="+18128182908",
            to="+919626338827"
        )
    print(message.status)
