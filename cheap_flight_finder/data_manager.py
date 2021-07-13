import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_endpoint = "https://api.sheety.co/cd2032a301bfec59875e473905557478/flightDeals/prices"
        self.sheet_data = self.get_all_flights()

    def get_all_flights(self):
        response = requests.get(self.sheet_endpoint)
        return response.json()

    def update_sheet(self, sheet_data):
        json = {
            "price": {
                "iataCode": f"{sheet_data['iataCode']}"
            }
        }
        response = requests.put(url=f"{self.sheet_endpoint}/{sheet_data['id']}", json=json)
        print(response.text)
