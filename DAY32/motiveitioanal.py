import datetime as dt
import smtplib
from random import choice



MY_EMAIL = "saeed@gmail.com"
PASSWORD = "something"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)


now = dt.datetime.now()
date = now.weekday()


with open("quotes.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


random_line = choice(content)

if date == 4:
    pass
    connection.sendmail(from_addr=MY_EMAIL
                        , to_addrs="saeed@gmail.com"
                        , msg=F"Subject:monday_motion\n\n {random_line}"
                        )





