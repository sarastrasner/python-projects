import datetime as dt
import random
import smtplib

# TODO: Monday Motivational Email
# TODO: create list of all lines of txt file
# TODO: check that the day of the week is the current day
# TODO: If it passes, send an email with a random quote from the quotes.text

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt", "r") as file:
        contents = file.readlines()
        random_quote = random.choice(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="strassy.email@yahoo.com",
            msg=f"Subject:Happy Monday!\n\nHappy Monday!\n{random_quote}")


