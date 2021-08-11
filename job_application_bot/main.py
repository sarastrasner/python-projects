from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

ACCOUNT_EMAIL = os.environ['ACCOUNT_EMAIL']
ACCOUNT_PASSWORD = os.environ['ACCOUNT_PASSWORD']
URL = 'https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=103644278&keywords=associate%20software' \
      '&location=United%20States '
PHONE = '225-368-5354'

chrome_driver_path = "/Users/sarastrasner/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(URL)

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()
print('Clicked on the apply button.')

# Review the application
time.sleep(5)
next_button = driver.find_element_by_css_selector("footer div button")
next_button.click()
print('Clicked on the next button.')

time.sleep(5)
footer_buttons = driver.find_elements_by_css_selector("footer div button")
review_button = footer_buttons[1]
review_button.click()
print('Clicked on the review button.')

# Submit the application
footer_buttons2 = driver.find_elements_by_css_selector("footer div button")
submit_button = footer_buttons2[1]
submit_button.click()
print('Clicked on the submit button.')

driver.quit()
