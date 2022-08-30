class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_data: dict, return_date: str):
        self.price = flight_data["price"]
        self.departure_code = flight_data["flyFrom"]
        self.arrival_city = flight_data["cityTo"]
        self.arrival_code = flight_data["flyTo"]
        self.outbound = flight_data['local_departure'].partition("T")[0]
        self.inbound = return_date.partition("T")[0]

    def __str__(self):
        return f"{self.arrival_city}: £{self.price}"
