import scrapy

class PostSpider(scrapy.Spider):
    name = "posts"
    
    start_urls = [
        'https://blog.scrapinghub.com/'
    ]

    # "self" is a method of this class
    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                # Extracts the title, date, and author from the blog above via the html/css tags
                'title': post.css('.post-header h2 a::text')[0].get(), 
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get() 
            }
        # Gets the link to the next page.
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        # print(dict(title=title,date=date,author=author)) 