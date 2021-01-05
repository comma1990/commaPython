# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Gif588KuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls=scrapy.Field()
    name=scrapy.Field()
    images = scrapy.Field()
