# imports the scrapy package
import scrapy

class HighPointsSpider(scrapy.Spider):
    # invoke spiders by their name
    name = "high_points"
    # the spider visits the follow urls to scrape information
    start_urls = [
        'https://www.peakbagger.com/list.aspx?lid=12004'
    ]
        
    def parse(self, response):
        # I want the first four columns of a table with class "gray"
        # I want to extract the text from a "tr" element
        rows = response.css('table.gray')
        for row in rows:
            print(row.css('tr')[0])    
# before running, make sure you're in the root "tutorial" directory
# to run, write "scrapy crawl quotes"

