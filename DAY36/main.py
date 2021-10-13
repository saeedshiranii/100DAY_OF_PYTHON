from twilio.rest import Client
import requests
import os


sid = "SKa61d808a1789ad7c9faf48e278c317fa"
secret = "Q79dr2aDI9tgwJ5hpJVXTl7KbUHedJNH"

my_key_stock = os.environ.get("MY_KEY_STOCK")
my_key_news = os.environ.get("MY_KEY_NEWS")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_number = os.environ.get("MY_NUMBER")
client = Client(account_sid, auth_token)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

item = {"function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": my_key_stock,
        "datatype": "json"}

print(requests.get(url="https://www.alphavantage.co/query", params=item))
stock_prices = requests.get(url="https://www.alphavantage.co/query", params=item).json()["Time Series (Daily)"]

stock_prices = list(stock_prices.items())

yesterday_price = float(stock_prices[0][1]["4. close"])
twe_day_ago_prince = float(stock_prices[1][1]["4. close"])

delta = abs(yesterday_price - twe_day_ago_prince)
if delta > ((twe_day_ago_prince * 5) / 100):
    news = requests.get(
        url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={my_key_news}").json()["articles"]

    news_list = []
    for new in news[:3:]:
        # news_list.append(new["url"])
        message = client.messages.create(
            body=new["url"],
            from_='+19149966113',
            to=my_number)
        print(message.sid)

# Optional TODO: Format the message like this:
"""
TESLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TESLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TESLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TESLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

