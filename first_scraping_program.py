import requests
from bs4 import BeautifulSoup
import csv

# Gets the website's HTML
response = requests.get("https://www.rithmschool.com/blog")

# Creates a new instance of BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Looks for all article tags within the website
articles = soup.find_all("article")

# Loop through each article...
for article in articles:

    # And get the text from each anchor tag
    title = article.find("a").get_text())
    href=article.find("a")
    # date =
