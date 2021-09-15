import datetime as dt
import pandas as pd
import smtplib
import random

# user email and password
MY_EMAIL = "your email"
PASSWORD = "your password"

""" create a secure connection and login into the users email"""
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)

""" check today's date and make a tuple for comprehension"""
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_date_tuple = (today_month, today_day)


""" read the csv of friends birthday and turn into a dict"""
birth_day_df = pd.read_csv("birthdays.csv")
day_column = birth_day_df.day
list_of_dicts = birth_day_df.to_dict(orient="records")

"""create a tuple with birthday_date and birthday_month for each  friend"""
for create in list_of_dicts:
    day_tuple = create["day"]
    month_tuple = create["month"]
    final_tuple = (month_tuple, day_tuple)
    create.update({"birth_date": final_tuple})

""" and finally append all birth_day tuples to empty list"""
list_of_tuple = []
for each_list in list_of_dicts:
    list_of_tuple.append(each_list["birth_date"])

""" check date of birth for each friend """
for friends_dict in list_of_dicts:
    if friends_dict['birth_date'] == today_date_tuple:  # if today was her/his birthday

        letter_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']  # choose a random letter
        chosen_letter = random.choice(letter_list)

        """ open the chosen letter and read it and replace the name of user's friend"""
        with open(F"letter_templates/{chosen_letter}") as letter:
            text = letter.read()
        text = text.replace("[NAME]", friends_dict['name'])
        with open(chosen_letter, "w") as letter:
            letter.write(text)
        with open(chosen_letter, "r") as letter:
            final_text = letter.read()

        """ and finally send the email for your friend"""
        friend_email = friends_dict['email']
        connection.sendmail(from_addr=MY_EMAIL
                            , to_addrs=friend_email
                            , msg=F"Subject: Happy Birthday then after \n\n {final_text}"
                            )
