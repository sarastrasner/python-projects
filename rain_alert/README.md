# Rain Alert
Checks the weather forecast for a given location, and sends me a text message if it will rain within the next 12 hours. 
Uses Twilio for sending SMS and the OpenWeather API for checking the forecast.

# Feature Tasks
1. Register with the OpenWeather API and use your API key to get the weather forecast for the next 12 hours.
1. If it will rain in the next 12 hours, print "Bring an umbrella"
1. Instead of printing, send a text message via Twilio. 
1. Save all keys and sensitive information as environmental variables.
1. Deploy this code and run it every morning with PythonAnywhere