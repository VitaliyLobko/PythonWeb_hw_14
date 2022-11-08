# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class QuotesItem(Item):
    keywords = Field()
    author = Field()
    quote = Field()
    author_description = Field()
    author_db = Field()
    author_location = Field()
