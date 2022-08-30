import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()

if dt.datetime.weekday(now) == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    my_email = "my-fake-email@gmail.com"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="my-fake-password")
        connection.sendmail(from_addr=my_email,
                            to_addrs="my-another-fake-email@yahoo.com",
                            msg=f"Subject:Motivation Monday\n\n{random.choice(quotes)}")

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv").to_dict(orient="records")

for row in data:
    if row["month"] == now.month and row["day"] == now.day:
        letter = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
        with open(letter) as file:
            text = file.read()

        text = text.replace("[NAME]", row["name"])
        my_email = "my-fake-email@gmail.com"
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password="my-fake-password")
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday!\n\n{text}")

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.
