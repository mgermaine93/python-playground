# Imports scrapy to use in project
import scrapy

# Every time a spider is created in this folder, scrapy is going to look here for the spiders to find.


class QuotesSpider(scrapy.Spider):

    # This refers to the name of the spider
    name = "quotes"

    # Loops through the URLs in the list and makes a request to each one
    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # This is the callback function referenced immediately above
    def parse(self, response):
        # Extracts the page number (last two characters) of the url that we're on
        page = response.url.split("/")[-2]
        # %s is an argument to which a string can be passed
        filename = 'quotes-%s.html' % page
        # Extracts the html content of the entire response that was sent back and saves to a file.
        with open(filename, 'wb') as f:
            f.write(response.body)
        # This is put out to the terminal
        self.log('Saved file %s' % filename)
