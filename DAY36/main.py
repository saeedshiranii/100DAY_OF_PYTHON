from twilio.rest import Client
import requests
import os


""" stock details """
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_key_stock = os.environ.get("MY_KEY_STOCK")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

""" News details """
my_key_news = os.environ.get("MY_KEY_NEWS")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


""" sms details """
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_number = os.environ.get("MY_NUMBER")
client = Client(account_sid, auth_token)

""" parameters for get data of stock """
item = {"function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": my_key_stock,
        "datatype": "json"}

""" get the data of stock """
stock_prices = requests.get(url="https://www.alphavantage.co/query", params=item).json()["Time Series (Daily)"]

""" find price of stock from data we got """
stock_prices = list(stock_prices.items())
yesterday_price = float(stock_prices[0][1]["4. close"])
twe_day_ago_prince = float(stock_prices[1][1]["4. close"])

""" find Changes of stock in last two days and if that change was bigger of 5% 
send link of three new in internet in three sms """

delta = abs(yesterday_price - twe_day_ago_prince)
if delta > ((twe_day_ago_prince * 5) / 100):
    news = requests.get(
        url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={my_key_news}").json()["articles"]

    news_list = []
    for new in news[:3:]:
        message = client.messages.create(
            body=new["url"],
            from_='phone number',
            to=my_number)
        print(message.sid)
