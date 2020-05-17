import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

####################################### Web Scraper ############################################

# All caps = constant
BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

####################################### GAME LOGIC ############################################


def start_game(quotes):
    # randomly picks a quote
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    guess = ''

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(
            f"Who said this? You have {remaining_guesses} guesses remaining. \n")
        # accounts for it the player guessed correctly
        if guess.lower() == quote["author"].lower():
            print("Well done!  You got it right!")
            break
        remaining_guesses -= 1
        print_hint(quote, remaining_guesses)

    play_again = ''
    while play_again not in ('y', 'yes', 'n', 'no'):
        play_again = input("Would you like to play again? (y/n) \n")
    if play_again.lower() in ('yes', 'y'):
        # begins the game again
        return start_game(quotes)
    else:
        print("OK, see you later! \n")


def print_hint(quote, remaining_guesses):
    # hint #1 = gives the author's birthday
    if remaining_guesses == 3:
        res = requests.get(f"{BASE_URL}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, features="html.parser")
        birthday = soup.find(class_="author-born-date").get_text()
        birthday_place = soup.find(
            class_="author-born-location").get_text()
        print(
            # the retrieved text already contains the missing "in"
            f"Not quite. Here's a hint: The author was born {birthday_place} on {birthday}.")
    # hint #2 = gives the author's birth location
    elif remaining_guesses == 2:
        first_initial = quote["author"][0]
        a = "a"
        if ["author"][0].lower() in ["a", "e", "f", "h", "i", "l", "m", "n", "o", "r", "s", "x"]:
            a = "an"
        print(
            f"Nope. Here's another hint:  The author's first name begins with {a} {first_initial} \n")
    # hint #3 = gives the first letter of the author's first name
    elif remaining_guesses == 1:
        a = "a"
        last_initial = quote["author"].split(" ")[1][0]
        if last_initial.lower() in ["a", "e", "f", "h", "i", "l", "m", "n", "o", "r", "s", "x"]:
            a = "an"
        print(
            f"Not quite. Here's your last hint:  The author's last name begins with {a} {last_initial} \n")
    else:
        print(
            f"Sorry, you ran out of guesses.  The answer is: {quote['author']} \n")


quotes = read_quotes("quotes.csv")
start_game(quotes)
