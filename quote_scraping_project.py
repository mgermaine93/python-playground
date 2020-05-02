import requests
from bs4 import BeautifulSoup
from time import sleep

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

# while the url is on a given page, make a request to that page.
while url:

    res = requests.get(f"{base_url}{url}")
    print(f"Scraping {base_url}{url}...")
    soup = BeautifulSoup(res.text, features="html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        all_quotes.append({
            # all text has class of "text"
            "text": quote.find(class_="text").get_text(),
            # all authors have class of "author"
            "author": quote.find(class_="author").get_text(),
            # retrieves the link to the author's biography
            "bio-link": quote.find("a")["href"]
        })

    next_button = soup.find(class_="next")
    # this will now be equal to the url that we'll find on the next page
    url = next_button.find("a")["href"] if next_button else None
    # this politely puts two seconds in-between each request -- prevents the overloading of the server
    sleep(2)

print(all_quotes)
