from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client
from datetime import datetime
from requests import get
from time import sleep
import os

END_POINT = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "something"
account_sid = "something"
auth_token = "something"


params = {
        "lat": "32.667461",
        "lon": "51.693501",
        "appid": api_key
        }


def search_api():
    get_response = get(END_POINT, params=params)
    get_response.raise_for_status()
    data = get_response.json()["hourly"]
    return data


def get_status():
    data = search_api()
    status = []
    for every_hour in data:
        whether_id = str(every_hour["weather"][0]["id"])
        status.append(whether_id[0])

    return status


def rain_check():
    status = get_status()
    next_14h = []
    for i in status[0:14]:
        next_14h.append(i)

    rainy = [2, 3, 5, 6]  # when it's raining (API documentation)
    for level in rainy:
        if str(level) in next_14h:
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body="Hi Dear\n Good morning \n Bring a Umbrella, Rain is possible...",
                from_="virtual number",
                to="real number"
            )
            print(message.status)


ON = True
while ON:

    hour = datetime.now().hour
    if hour == 6:
        rain_check()
    sleep(3600)  # every one hour

