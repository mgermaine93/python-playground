# Imports scrapy to use in project
import scrapy

# Every time a spider is created in this folder, scrapy is going to look here for the spiders to find.


class QuotesSpider(scrapy.Spider):

    # This refers to the name of the spider
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

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
