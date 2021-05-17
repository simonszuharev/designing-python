# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import requests
from datetime import date
from datetime import timedelta

STOCK = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
STOCK_API_KEY = "__YOUR___API___KEY"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "__YOUR___API___KEY"

# Twilio msg
account_sid = '__YOUR___SID___KEY'
auth_token = '__YOUR___AUTH___TOKEN'
client = Client(account_sid, auth_token)
## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

# getting the stock data
response_for_stock = requests.get(
    url=f"{STOCK_ENDPOINT}?function={STOCK_FUNCTION}&symbol={STOCK}&apikey={STOCK_API_KEY}")
response_for_stock.raise_for_status()
stock_data = response_for_stock.json()

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.

# getting news data
response_for_news = requests.get(url=f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}")
response_for_news.raise_for_status()
news_data = response_for_news.json()

first_three_articles = []
for article in range(0, 3):
    dict = {"title": news_data['articles'][article]['title'],
            "description": news_data['articles'][article]['description'],
            "url": news_data['articles'][article]['url']}

# getting today's data
today = date.today()
yesterday: date
day_before_yesterday: date

if today.weekday() == 0:
    yesterday = today - timedelta(days=3)
    day_before_yesterday = today - timedelta(days=4)
elif today.weekday() == 6:
    yesterday = today - timedelta(days=2)
    day_before_yesterday = today - timedelta(days=3)
else:
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)

yesterday_data = stock_data["Time Series (Daily)"][str(yesterday)]['4. close']
day_before_yesterday_data = stock_data["Time Series (Daily)"][str(day_before_yesterday)]['4. close']


difference = round(float(yesterday_data) - float(day_before_yesterday_data), 2)
difference_percent = round((float(yesterday_data) / float(day_before_yesterday_data) - 1) * 100, 2)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.
if difference_percent > 0:
    first_line = f"TSLA: 🔺{difference_percent}%\n"
else:
    first_line = f"TSLA: 🔻{difference_percent}%\n"


for info in first_three_articles:
    message = client.messages \
        .create(
        body=f"{first_line}"
             f" HEADLINE: {info['title']}\n"
             f"BRIEF: {info['description']}\n"
             f"URL: {info['url']}",
        from_='__SENDER__PHONE___NUMBER',
        to='__YOUR__PHONE___NUMBER'
    )

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
