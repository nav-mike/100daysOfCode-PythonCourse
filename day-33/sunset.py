import requests

response = requests.get("https://api.sunrise-sunset.org/json", params={"lat": 60.165370, "lng": 24.651610})
response.raise_for_status()
print(response.json())
