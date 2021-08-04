# Amazon Price Tracker
An automated price tracker that uses BeautifulSoup to monitor the price of a given item on Amazon. If the price drops below a specified threshold, smtplib emails me with the price and item name.

## Feature Tasks
1. Find a product on Amazon that you want to track and get the product URL.
1. Use the `requests` library to request the HTML page of the Amazon product using the URL you got from 1.
1. Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml" parser instead of the "html.parser" for this to work.
1. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
1. When the price is below your purchase threshold, then use the smtp module to email yourself. In the email, include the title of the product, the current price and a link to buy the product.

