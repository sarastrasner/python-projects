from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
# all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")

for listing in all_listings:
    print("found a job")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
