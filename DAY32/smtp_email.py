import smtplib

MY_EMAIL = "saeedbypython@gmail.com"
PASSWORD = "alijonkonghermeze"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)
connection.sendmail(from_addr=MY_EMAIL
                    , to_addrs="saeed@gmail.com"
                    , msg="Subject:s_p\n\n This is me."
                    )

connection.close()
