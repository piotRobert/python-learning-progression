from datetime import datetime
from dotenv import load_dotenv
import os
import pandas
import random
import smtplib

load_dotenv()
MY_EMAIL = os.getenv("EMAIL_ADDRESS")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("d32_automation_mail_sender/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"d32_automation_mail_sender/letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person['email'],
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
        



