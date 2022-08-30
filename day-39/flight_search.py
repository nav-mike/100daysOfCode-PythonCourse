import requests
from datetime import datetime, timedelta

from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key: str):
        self.city_search_url = "https://tequila-api.kiwi.com/locations/query"
        self.flights_search_url = "https://tequila-api.kiwi.com/v2/search?"
        self.api_key = api_key

    def search_city(self, city: str) -> str:
        response = requests.get(self.city_search_url,
                                params={"term": city, "location_types": "city"},
                                headers={"apikey": self.api_key})
        response.raise_for_status()

        return response.json()['locations'][0]['code']

    def search_flights(self, city: str) -> FlightData:
        response = requests.get(self.flights_search_url,
                                params={"fly_from": "LON",
                                        "fly_to": city,
                                        "date_from": datetime.now().strftime("%d/%m/%Y"),
                                        "date_to": (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
                                        "nights_in_dst_from": 7,
                                        "nights_in_dst_to": 28,
                                        "adults": 1,
                                        "curr": "GBP",
                                        "sort": "price"},
                                headers={"apikey": self.api_key})
        response.raise_for_status()

        return FlightData(response.json()['data'][0], response.json()['data'][0]['local_departure'])
