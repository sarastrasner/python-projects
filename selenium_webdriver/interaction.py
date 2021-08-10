# TODO: Print the article count from Wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/sarastrasner/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
count = driver.find_element_by_css_selector("#articlecount a")
# count.click()
# print(count.text)

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()

