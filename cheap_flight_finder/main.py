#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
data_manager = DataManager()
flight_search = FlightSearch()

pprint(data_manager.sheet_data)

for city in data_manager.sheet_data:
    if not city['iataCode']:
        city['iataCode'] = flight_search.get_iata_code(city['city'])
        data_manager.update_sheet(city)

print(data_manager.sheet_data)
# You should use the response from the FlightSearch class to update the sheet_data dictionary.