# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pass


# class MyItem(scrapy.Item):
#     # ... other item fields ...
#     image_urls = scrapy.Field()
#     images = scrapy.Field()