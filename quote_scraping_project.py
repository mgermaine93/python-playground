# http://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup

res = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(res.text)
quotes = soup.find_all(class_="quote")
print(quotes)
