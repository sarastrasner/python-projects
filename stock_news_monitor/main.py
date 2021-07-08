import requests
import datetime
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
MY_NUMBER = os.getenv('MY_NUMBER')

today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}'
r = requests.get(url)
r.raise_for_status()
data = r.json()['Time Series (Daily)']
data_list = [(key, float(value['4. close'])) for (key, value) in data.items()]

yesterday_closing = data_list[0]

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing = data_list[1]
# print(yesterday_closing, day_before_yesterday_closing)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
price_difference = round(abs(yesterday_closing[1] - day_before_yesterday_closing[1]), 2)
if yesterday_closing[1] - day_before_yesterday_closing[1] > 0:
    difference_symbol = "🔺"
else:
    difference_symbol = "🔻"

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
price_difference_percentage = round(price_difference / yesterday_closing[1] * 100, 2)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if price_difference_percentage < 5:
    print("Get news")
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from{today}&sortBy=popularity&apiKey={NEWS_API_KEY}")
    response.raise_for_status()

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    articles = response.json()['articles'][:3]

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    headlines = [(item['title'], item['description']) for item in articles]
    print(headlines)

    # TODO 9. - Send each article as a separate message via Twilio.
    for item in headlines:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {difference_symbol}{price_difference_percentage}%\nHeadline: {item[0]}\nBrief {item[1]}",
            from_='+16789819663',
            to=MY_NUMBER
        )

        print(message.status)
else:
    print(f"No major difference ({price_difference_percentage}% {difference_symbol}) in {COMPANY_NAME} stock")

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
