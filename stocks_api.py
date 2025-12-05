import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

CRYPTO_NEWS_PARAMETERS = {
    'apiKey': NEWS_API_KEY,
    'q': 'Bitcoin',
    'searchIn': 'title,content',
    'from': str(datetime.date.today() - datetime.timedelta(days=2)),
    'to': str(datetime.date.today()),
    'language': 'en',
    'sortBy': "relevancy",
}

crypto_news_response = requests.get(url=NEWS_ENDPOINT, params=CRYPTO_NEWS_PARAMETERS)
crypto_news_response.raise_for_status()
crypto_news_data = crypto_news_response.json()
print(crypto_news_data.prettify)