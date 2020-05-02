import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

####################################### Web Scraper ############################################

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

# while the url is on a given page, make a request to that page.
while url:

    res = requests.get(f"{base_url}{url}")
    # print(f"Scraping {base_url}{url}...")
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
    # sleep(2)

####################################### GAME LOGIC ############################################

# randomly picks a quote
quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote: ")
print(quote["text"])
print(quote["author"])
guess = ''

while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(
        f"Who said this? You have {remaining_guesses} guesses remaining. \n")
    remaining_guesses -= 1
    # hint #1 = gives the author's birthday
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, features="html.parser")
        birthday = soup.find(class_="author-born-date").get_text()
        birthday_place = soup.find(class_="author-born-location").get_text()
        print(
            # the retrieved text already contains the missing "in"
            f"Here's a hint: The author was born {birthday_place} on {birthday}.")
    # hint #2 = gives the author's birth location
    # hint #3 = gives the first letter of the author's first name
    # hint #4 = gives the first letter of the author's last name
print("AFTER WHILE LOOP")
