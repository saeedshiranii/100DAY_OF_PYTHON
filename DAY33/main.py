import datetime as dt
import time as tt
import requests
import smtplib
""" """

MY_LTN = 32.654629  # User Latitude
MY_LNG = 51.667984  # User Longitude
MY_EMAIL = "saeedbypython@gmail.com"  # User Email
MY_PASS = "alijonkonghermeze"  # User Email Password

""" Create a connection """
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASS)

""" get local information about sunset and sunrise """
location_parameters = {"lnt": MY_LTN, "lng": MY_LNG, "formatted": 0}
respond = requests.get('https://api.sunrise-sunset.org/json', params=location_parameters)
respond.raise_for_status()
sunrise_time = int(respond.json()['results']['sunrise'].split("T")[1].split(":")[0])
sunset_time = int(respond.json()['results']['sunset'].split("T")[1].split(":")[0])


def iss_is_above_you():
    """
    find and return exact position of Iss and current user local time
    :return:
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_position = iss_data['iss_position']
    iss_latitude = float(iss_position['latitude'])
    iss_longitude = float(iss_position['longitude'])

    time = dt.datetime.now()
    local_hour = int(time.hour)
    return [iss_latitude, iss_longitude, local_hour]


""" check time and distance of user and iss and send email if every thing was right """
send_letter = True
while send_letter:
    get = iss_is_above_you()
    if (MY_LNG-5 < get[1] < MY_LNG+5) and (MY_LTN-5 < get[1] < MY_LTN+5):
        if get[2] > 19 or get[2] < 5:
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL
                                , msg="Subject:LOOK UP \n\n Iss in above your head.")
            print("Done.")
            send_letter = False
            break

    else:
        tt.sleep(1)
        continue

