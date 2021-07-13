import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com/"

    def get_iata_code(self, city):
        print(f"Get IATA code received: {city}")
        headers_dict = {
            "apikey": "uS1uuDpkVIAzlML4da9fg6KDKPsL2G6_"
        }
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=f"{self.tequila_endpoint}/locations/query", headers=headers_dict, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

