from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/sarastrasner/Development/chromedriver"

FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSd8SnH_bYEbxJtyFSErTh9BVtv4xE1H-oM5Mk8cdst4H-TKBQ/viewform?usp' \
            '=sf_link '
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/2-_beds/1.0-_baths/?searchQueryState=%7B%22mapBounds%22%3A%7B' \
             '%22west%22%3A-70.35763913263948%2C%22east%22%3A-70.20245724787385%2C%22south%22%3A43.63275940262426%2C' \
             '%22north%22%3A43.69013300955387%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A' \
             '%7B%22max%22%3A823461%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C' \
             '%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value' \
             '%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc' \
             '%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22' \
             '%3A2%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C' \
             '%22pagination%22%3A%7B%7D%7D '
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


class DataEntry:
    def __init__(self):
        self.all_links = []
        self.all_prices = []
        self.all_addresses = []

    def get_data(self):
        response = requests.get(ZILLOW_URL, headers=header).text
        soup = BeautifulSoup(response, 'html.parser')
        # print(soup.prettify())

        results = soup.find_all(class_="list-card-info")
        print(results)

        [self.all_prices.append(item.text.split('+')[0].split('/')[0]) for item in soup.select('.list-card-price')]
        # print(f'{len(all_prices)}')

        [self.all_addresses.append(item.text.split(" | ")[-1]) for item in soup.select('.list-card-addr')]
        # print(f'{len(all_addresses)}')

        all_link_elements = soup.select(".list-card-top a")
        for link in all_link_elements:
            href = link["href"]
            if "http" not in href:
                self.all_links.append(f"https://www.zillow.com{href}")
            else:
                self.all_links.append(href)
        # print(f'{len(all_links)}')

    def fill_form(self):
        driver = webdriver.Chrome(executable_path=chrome_driver_path)

        for n in range(len(self.all_addresses)):
            driver.get(FORM_LINK)
            address = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
            address.send_keys(self.all_addresses[n])
            price.send_keys(self.all_prices[n])
            link.send_keys(self.all_links[n])
            submit_button.send_keys(Keys.ENTER)

        driver.quit()


bot = DataEntry()
bot.get_data()
bot.fill_form()
