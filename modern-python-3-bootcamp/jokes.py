# Import the requests module
import requests

# Import the random module
from random import choice

# Import figlet_format
from pyfiglet import figlet_format

# Import term color
from termcolor import colored

# Prints and formats the header
header = figlet_format("DAD JOKE O-MATIC!")
header = colored(header, color="cyan")
print(header)

#Ask the user for input
user_input = input("What do you want me to joke about? ")

# Gets the URL of the site
url = "https://icanhazdadjoke.com/search"

# Saves the response to a JSON-formatted variable
results = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

# Captures the total jokes returned from the request
num_jokes = results["total_jokes"]

# Sets the results equal to a variable
retrieved_results = results["results"]

# Accounts for many, one, or no jokes
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}.  Here's a good one: ")
    print(choice(retrieved_results)['joke'])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}.  Ready?  Here goes: ")
    print(retrieved_results[0]['joke'])
else:
    print(f"Sorry, I couldn't find a joke about {user_input}")
