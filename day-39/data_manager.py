import requests
from pprint import pprint

from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_search: FlightSearch, sheet_url: str):
        self.data = {}
        self.sheet_url = sheet_url
        self.flight_search = flight_search

    def load(self) -> None:
        response = requests.get(self.sheet_url)
        response.raise_for_status()

        self.data = response.json()["prices"]

    def print(self) -> None:
        pprint(self.data)

    def any_has_not_iata(self) -> bool:
        for item in self.data:
            if item["iataCode"] == "" or item["iataCode"] == "TESTING":
                return True
        return False

    def update_iata_code(self) -> None:
        if not self.any_has_not_iata():
            return

        for item in self.data:
            item["iataCode"] = self.flight_search.search_city(item["city"])
            self.update_item(item, item["id"])

    def update_item(self, item: dict, index: int) -> None:
        response = requests.put(f"{self.sheet_url}/{index}", json={"price": item})
        response.raise_for_status()


