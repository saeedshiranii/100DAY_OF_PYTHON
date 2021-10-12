import newsapi
import requests
import os

my_key_stock = os.environ.get("MY_KEY_STOCK")
my_key_news = os.environ.get("MY_KEY_NEWS")

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
    news = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={my_key_news}").json()
    print(news)
## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

