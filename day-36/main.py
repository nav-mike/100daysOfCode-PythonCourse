import requests
import os
from dotenv import load_dotenv
# from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_VANTAGE_API_KEY}")
response.raise_for_status()

data = response.json()

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday = '2022-07-15'  # (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
before_yesterday = '2022-07-14'  # (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")

ytd_value = float(data['Time Series (Daily)'][yesterday]['4. close'])
before_ytd_value = float(data['Time Series (Daily)'][before_yesterday]['4. close'])

diff = ytd_value - before_ytd_value
value = diff / before_ytd_value * 100

if value >= 5:
    print("Get News")

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
response = requests.get(f"https://newsapi.org/v2/everything", params={"qInTitle": COMPANY_NAME, "apiKey": NEWS_API_KEY})
response.raise_for_status()

news_data = response.json()

news = [{"title": item["title"], "content": item["description"]} for item in news_data["articles"][:3]]

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

if diff > 0:
    emoji = "🔺"
else:
    emoji = "🔻"

message = f"{STOCK}: {emoji}{value:.2f}%\n"

for item in news:
    message += f"Headline: {item['title']}\nBrief: {item['content']}\n"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(body=message,
                                 from_=os.getenv("FROM_PHONE_NUMBER"), to=os.getenv("TO_PHONE_NUMBER"))
print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
