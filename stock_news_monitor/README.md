# Stock News Monitor
An application that checks the closing stock prices for a given stock. If the closing stock price has fluctuated by over
5% in the last two days, it sends a text with the percentage difference, and the 3 latest news articles about that company.
Built using Alpha Vantage API, News API, Twilio, requests, and datetime. 

![Stock Alert Texts](stock_alert_texts.png)

## Feature Tasks
1. Pull in the stock prices of the stocks we're interested in.
    1. Pull in closing price on yesterday and previous day
   1. Find the percentage difference between the two prices.
1. If the above percentage difference is greater than 5, fetch the news data related to that company.
   1. Only keep the first three articles' headlines and descriptions.
1. Send each article as a separate SMS.