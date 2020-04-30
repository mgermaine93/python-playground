import requests
from bs4 import BeautifulSoup

all_quotes = []
res = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(res.text, features="html.parser")
quotes = soup.find_all(class_="quote")
for quote in quotes:
    all_quotes.append({
        # all text has class of "text"
        "text": quote.find(class_="text").get_text(),
        # all authors have class of "author"
        "author": quote.find(class_="author").get_text()
    })

print(all_quotes)
