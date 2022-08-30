from dotenv import load_dotenv
import os

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()

fs = FlightSearch(os.getenv("TEQUILA_API_KEY"))
dm = DataManager(fs, os.getenv("SHEETY_URL"))
dm.load()
dm.update_iata_code()

for item in dm.data:
    fd = fs.search_flights(item["iataCode"])
    print(fd)
    if item['lowestPrice'] >= fd.price:
        nm = NotificationManager(fd)
        nm.notify(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"),
                  os.getenv("FROM_PHONE_NUMBER"), os.getenv("TO_PHONE_NUMBER"))

