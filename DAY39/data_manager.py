from email import header
from pprint import pprint
import requests


SHEET_ENDPOINT= "https://api.sheety.co/48f940685b4d46591451697f484b9079/flightDeals/sheet1"
HEADER= {"Content-Type":"application/json",
                "Authorization": "Bearer qwertyuiasdfghjkqsdcvwerty748596857445742955"
                }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.location_data = {}
        
    def resive_data(self):
        
                
        responce =requests.get(url=SHEET_ENDPOINT, headers=HEADER)
        sheet_data = responce.json()
        self.location_data = sheet_data["sheet1"]
        return self.location_data


    def update_destination_codes(self):
            for city in self.location_data:
                new_data = {
                    "sheet1": {
                        "iataCode": city["iataCode"]
                    }
                }
                response = requests.put(
                    url=f"{SHEET_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers= HEADER
                )
                print(response.text)

