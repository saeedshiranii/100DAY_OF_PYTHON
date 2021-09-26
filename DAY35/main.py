from requests import get
from datetime import datetime
from time import sleep

MY_API = "https://api.openweathermap.org/data/2.5/onecall?" \
         "lat=32.667461&lon=51.693501&appid=e07f0e58532e56ed1d207642431d7b1b"


def search_api():
    get_response = get(url=MY_API)
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
        if level in next_14h:
            print("Hi Dear\n Good morning \n Bring a Umbrella, Rain is possible...")


ON = True
while ON:

    hour = datetime.now().hour
    if hour == 6:
        rain_check()
    sleep(3600)  # every one hour

