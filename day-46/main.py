import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B07RTSW8JS/ref=syn_sd_onsite_desktop_154?ie=UTF8&psc=1&pd_rd_plhdr=t"

response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
})
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.select_one(selector="div.a-section span.a-price span.a-offscreen").get_text().replace("$", ""))
print(price)

if price < 30:
    print("Buy it!")  # send email here
else:
    print("Too expensive!")
