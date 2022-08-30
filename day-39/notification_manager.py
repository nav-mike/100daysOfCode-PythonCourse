from flight_data import FlightData
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, fd: FlightData):
        self.fd = fd

    def notify(self, account_sid: str, auth_token: str, from_: str, to: str) -> None:
        message = f"Low price alert! Only £{self.fd.price} to fly from London-{self.fd.departure_code} to {self.fd.arrival_city}-{self.fd.arrival_code}, from {self.fd.outbound} to {self.fd.inbound}."
        client = Client(account_sid, auth_token)
        client.messages.create(body=message, from_=from_, to=to)
