from selenium import webdriver
import re
from send_email import send_email

chrome_driver_path = "/Users/sarastrasner/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

ZIP_CODE = 80016
SEARCH_DISTANCE = 20
# QUERY = 'adjustable%20dumbbells'
QUERY = 'adjustable%20dumbbells%20power%20block'


driver.get(
    f"https://denver.craigslist.org/search/spo?postal={ZIP_CODE}&query={QUERY}&search_distance={SEARCH_DISTANCE}")
prices = driver.find_elements_by_class_name("result-price")

items = []
send_message = False

for price in prices:
    price_as_int = int(re.sub("[^0-9]", "", price.text))
    if price_as_int < 500 and price_as_int not in items:
        send_message = True
        items.append(price_as_int)

if send_message:
    send_email(items)

driver.quit()
