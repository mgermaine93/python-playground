import requests
from bs4 import BeautifulSoup
from csv import writer

# Gets the website's HTML
response = requests.get("https://www.rithmschool.com/blog")

# Creates a new instance of BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Looks for all article tags within the website
articles = soup.find_all("article")

# "w" = write mode
with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow("title", "link", "date")

    # Loop through each article...
    for article in articles:
        # And get the text from each anchor tag...
        a_tag = article.find("a")
        # title tag...
        title = a_tag.get_text()
        # href tag...
        link = a_tag['href']
        # and date
        date = article.find("time")["datetime"]

        csv_writer.writerow([title, link, date])
