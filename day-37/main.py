import requests
import os
from dotenv import load_dotenv

load_dotenv()

user_params = {
    "token": os.getenv("PIXELA_PASSWORD"),
    "username": os.getenv("PIXELA_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post('https://pixe.la/v1/users', json=user_params)
# print(response.json())

# response = requests.post(f"https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs",
#                          json={
#                              "id": os.getenv("PIXELA_GRAPH_ID"),
#                              "name": "Cycling Graph",
#                              "unit": "km",
#                              "type": "float",
#                              "color": "sora"
#                          }, headers={"X-USER-TOKEN": os.getenv("PIXELA_PASSWORD")})
# print(response.json())

response = requests.post(
    f"https://pixe.la/v1/users/{os.getenv('PIXELA_USERNAME')}/graphs/{os.getenv('PIXELA_GRAPH_ID')}",
    json={"date": "20220718", "quantity": "22.5"}, headers={"X-USER-TOKEN": os.getenv("PIXELA_PASSWORD")}
)
print(response.json())
