# imports the scrapy package
import scrapy

class QuotesSpider(scrapy.Spider):
    # invoke spiders by their name
    name = "high_points"
    def start_requests(self):
        # the spider visits the follow urls to scrape information
        start_urls = [
            'https://www.peakbagger.com/list.aspx?lid=12004'
        ]
        # loops through the urls in the list above and make a request using scrapy
        for url in start_urls:
            # pass in the url as well as the callback function to perform on the url
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # this grabs the page number listed in each url above (1, 2, etc.)
        # page = response.url.split("/")[-2]
        # %s is an argument to which "page" is passed
        # filename = 'high_points-%s.html' % page
        filename = 'high_points.html'
        # this extracts the html content (body) from the page and writes it to a file
        with open(filename, 'wb') as f:
            f.write(response.body)
        # prints out to the terminal when the spider runs
        self.log('Saved file %s' % filename)

# before running, make sure you're in the root "tutorial" directory
# to run, write "scrapy crawl quotes"

