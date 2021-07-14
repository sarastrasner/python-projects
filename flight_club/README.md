# Flight Club
A continuation of the [Cheap Flight Finder project](https://github.com/sarastrasner/python-projects/tree/main/cheap_flight_finder) that accomodates multiple users, handles exceptions, handles destinations without direct flights, and emails all users when deals arise. 

# Feature Tasks
1. Create the customer acquisition code on [Repl.it](https://replit.com/@SaraStrasner/Flight-Club-Signup#main.py). This is how new users will sign up for our service and be added to the Google Sheet of all users.
    1. Use the Sheety API to POST the data that the user enters into the user sheet in your Copy of Flight Deals Google Sheet.
1. For some destinations, certain time periods, there will be no flights available. We need to add exception handling to our code so that it doesn't break and crash in these situations.
1. Handle destinations without direct flights:
   1. If a flight is not found, check to see if there are flights with 1 stop and pretty print the result with pprint().
   1. Modify the FlightData class to add 2 optional init parameters with default values - stop_overs=0 and via_city="" . Instead of the printing the result from (1.) above, create a flight object with stop_overs set to 1 and via_city as the name of stopover city. Examine the data you printed in (1.) carefully to extract the information for origin_city, origin_airport, destination_city, destination_airport, out_date, and return_date .
1. Notify all customers when there is a good deal.