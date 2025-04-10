# Motivation monday script - sending mail with motivation quote

import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import pandas
import random

load_dotenv()
my_email = os.getenv("EMAIL_ADDRESS")
my_password = os.getenv("EMAIL_PASSWORD")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("d32_automation_mail_sender/quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        random_quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mail",
            msg=f"Subject: Motivation quote\n\n {random_quote} \n now you subscribed to recive motivation quote every monday :)"
        )
    print(type(quote_list))

date_of_birth = dt.datetime(year=2003 , month=7 , day=21)
