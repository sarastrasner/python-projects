from selenium import webdriver
import re
import smtplib
import os

chrome_driver_path = "/Users/sarastrasner/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

ZIP_CODE = 80016
SEARCH_DISTANCE = 20
QUERY = 'adjustable%20dumbbells'
# QUERY = 'adjustable%20dumbbells%20power%20block'

# MY_EMAIL = os.getenv('MY_EMAIL')
# PASSWORD = os.getenv('PASSWORD')

driver.get(
    f"https://denver.craigslist.org/search/spo?postal={ZIP_CODE}&query={QUERY}&search_distance={SEARCH_DISTANCE}")
prices = driver.find_elements_by_class_name("result-price")

items = []
send_message = False


def send_email(content):
    print("send email function triggered")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        toaddr = "girliesara22@yahoo.com"
        bcc = ['sarastrasner@gmail.com']
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=[toaddr] + bcc,
            msg=f"Subject: TEST\nTEST!!!")


for price in prices:
    price_as_int = int(re.sub("[^0-9]", "", price.text))
    if price_as_int < 500 and price_as_int not in items:
        send_message = True
        items.append(price_as_int)

if send_message:
    send_email(items)

driver.quit()

