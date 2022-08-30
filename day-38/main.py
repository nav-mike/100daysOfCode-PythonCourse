from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()

activity = input("Tell me which exercises you did: ")

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json={
    "query": activity,
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 176,
    "age": 31
}, headers={
    "x-app-id": os.getenv("NUTRITIONOX_APP_ID"),
    "x-app-key": os.getenv("NUTRITIONOX_API_KEY")
})
response.raise_for_status()

data = response.json()

for item in data["exercises"]:
    sheety_response = requests.post(os.getenv("SHEETY_URL"),
                                    json={"workout": {
                                        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
                                        "time": datetime.datetime.now().strftime("%X"),
                                        "exercise": item["name"].title(),
                                        "duration": item["duration_min"],
                                        "calories": item["nf_calories"]}},
                                    headers={"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"})
    sheety_response.raise_for_status()

