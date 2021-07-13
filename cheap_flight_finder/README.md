# Cheap Flight Finder Pt I
APIs Required
Google Sheet Data Management - https://sheety.co/
Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
Twilio SMS API - https://www.twilio.com/docs/sms

# Feature Tasks
1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
1. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
1. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
1. The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.
1. Toggle these options when setting up with the API providers
1. Avoid making too many unnecessary requests with the Sheety API while testing your code. The free tier for the Sheety API only allows 200 requests per month.
1. Also, enable the PUT option so that you can write to your Google sheet
1. Register with the Kiwi Partners Flight Search API
1. Your account name should be the same as what you used later in "First name" and "Last name".
1. There is no need to provide a credit card or billing information (you can skip that section) when you create your "Solution" (previously called "Application").
1. When registering for your API key choose Meta Search as your product type.
1. Then choose One-Way and Return.

