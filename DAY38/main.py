import json
import requests



APP_ID = "465f8448"
APP_KEYS = "2398f86ba20f9a6c338ba78806d3060b"
NUTRI_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
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
print(user_result)
