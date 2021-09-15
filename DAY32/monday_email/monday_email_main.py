import datetime as dt
import smtplib
from random import choice

""" this program should each monday send a beautiful sentence for your friends"""
MY_EMAIL = "saeed@gmail.com"
PASSWORD = "something"

""" make connection"""
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)


with open("quotes.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

""" check today is monday or not """
random_line = choice(content)
now = dt.datetime.now()
monday = 1
day = now.weekday()

""" send email if it's monday"""
if day == monday:
    connection.sendmail(from_addr=MY_EMAIL
                        , to_addrs="saeed@gmail.com"
                        , msg=F"Subject:monday_motion\n\n {random_line}"
                        )





