from email import header
from datetime import datetime
import json
import requests



APP_ID = "465f8448"
APP_KEYS = "2398f86ba20f9a6c338ba78806d3060b"
NUTRI_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/48f940685b4d46591451697f484b9079/myworkout/sheet1"
user_answer = input("how many exercise you did to day?")


api_parameters = {
    "query": user_answer,
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}
api_header = {
    "x-app-id" : APP_ID,
    "x-app-key": APP_KEYS,
    "x-remote-user-id": "0"

}

respuance = requests.post(url=NUTRI_API_ENDPOINT, json = api_parameters , headers= api_header)
user_result = respuance.json()


today = datetime.now()
date = f"{today.strftime('%d')}\{today.strftime('%m')}\{today.strftime('%Y')}"
time = today.strftime('%X')


for exercise in user_result["exercises"]:
    workouts = {
        "sheet1":{
        "calories":exercise['nf_calories'],
        "duration":exercise['duration_min'],
        "exercise":exercise['name'].title(),
        "time":time,
        "date":date
        }}


sheet_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer lkjhgfdssdfghjkiuytrertyuiiuytre748596",
}

sheet_respuance = requests.post(url=SHEET_ENDPOINT, json= workouts, headers=sheet_header)
print(sheet_respuance.text)








