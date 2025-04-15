import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
APIKEY_APLHA = os.getenv("API_KEY_ALPHAVANTAGE")
APIKEY_NEWS = os.getenv("API_KEY_NEWSAPI")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API = "https://www.alphavantage.co/query"
NEWS_API = "https://newsapi.org/v2/everything"

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": APIKEY_APLHA
}

alpha_response = requests.get(ALPHA_API, params=alpha_params)
alpha_response.raise_for_status()
data = alpha_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()] 
yeasterday_data = data_list[0]
yeasterday_closing_price = yeasterday_data["4. close"]

day_before_yeasterday_data = data_list[1]
day_before_yeasterday_closing_price = day_before_yeasterday_data["4. close"]

diff = float(yeasterday_closing_price) - float(day_before_yeasterday_closing_price)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((diff / float(yeasterday_closing_price)) *100)
if abs(diff_percent) >= 5:
    news_params = {
        "apiKey": APIKEY_NEWS,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_API, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"\n{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="{phone_number}",
            to="{phone_number}",
        )