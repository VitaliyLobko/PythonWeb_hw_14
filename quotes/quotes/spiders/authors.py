import scrapy
from ..items import QuotesItem


class AuthorsSpider(scrapy.Spider):

    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        name = 'authors'
        allowed_domains = ['quotes.toscrape.com']
        start_urls = ['http://quotes.toscrape.com/']

        quotes = response.xpath("/html//div[@class='quote']")

        for quote in quotes:
            item = QuotesItem()
            item['keywords'] = quote.xpath("div[@class='tags']/a/text()").extract()
            item['author'] = str(quote.xpath("span/small/text()").get()).replace('`', '')
            item['quote'] = quote.xpath("span/text()").get()

            author_link = quote.xpath("span/a").attrib['href']

            if author_link:
                yield scrapy.Request(url=self.start_urls[0] + author_link, callback=self.parse_author)

            yield item

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
            item = QuotesItem()
            item['author_description'] = str(response.xpath("//div[@class='author-description']/text()").get()).strip()
            item['author_db'] = str(response.xpath("//span[@class='author-born-date']/text()").get()).strip()
            item['author_location'] = str(response.xpath("//span[@class='author-born-location']/text()").get()).strip()
            yield item
