import requests
from datetime import datetime, timedelta
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "3FBFDWXLIRMN49OW"
NEWS_API_KEY = "66ae0203c28f41e694d920a6bea9184d"
TWILIO_ACCOUNT_SID = "ACb0efc8ed8dcf40654f4f67412a690fda"
TWILIO_AUTH_TOKEN = "49192f670fb8ed0600434bef81965e5b"
TWILIO_PHONE_NUMBER = "+12183062962"
RECEIVER_PHONE_NUMBER = "+61480578314"

# STEP 1: Get yesterday's and the day before yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# STEP 2: Calculate the percentage difference between the closing prices
price_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
percentage_difference = (price_difference / yesterday_closing_price) * 100

# STEP 3: Get news if the percentage difference is greater than 5%
if percentage_difference > 5:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    top_three_articles = articles[:3]

    # STEP 4: Send each article as a separate message via Twilio
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in top_three_articles:
        title = article["title"]
        description = article["description"]
        direction = "🔺" if yesterday_closing_price > day_before_yesterday_closing_price else "🔻"
        message_body = f"{STOCK_NAME}: {direction}{percentage_difference:.2f}%\n\nHeadline: {title}\n\nBrief: {description}"
        client.messages.create(
            to=RECEIVER_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            body=message_body
        )
