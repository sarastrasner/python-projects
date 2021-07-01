import datetime as dt
import random
import smtplib
import pandas

# TODO 1. Update the birthdays.csv with your friends & family's details.

# TODO 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# TODO 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from
#  letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person['name']
    print(f"Found one! It's {name}'s birthday!")
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_template:
        contents = letter_template.read()
        customized_letter = contents.replace("[NAME]", f"{name}")
    # TODO 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        toaddr = f"{birthday_person['email']}"
        bcc = ['sarastrasner@gmail.com']
        connection.sendmail(
            from_addr=my_email,
            to_addrs=[toaddr] + bcc,
            msg=f"Subject:Go {name}, it's your birthday!\n\n{customized_letter}")
