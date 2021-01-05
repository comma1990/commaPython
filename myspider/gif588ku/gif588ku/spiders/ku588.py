import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Gif588KuItem
'''
gif=//a[@class="img-box"]/@href
gif=//div[@class="img-box gif"]/img/@src

'''
class Ku588Spider(CrawlSpider):
    name = 'ku588'
    allowed_domains = ['588ku.com']
    start_urls = ['http://588ku.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://588ku.com/gif/0-0-0-default-1/'),  follow=True),
        Rule(LinkExtractor(allow=r'/gif1/\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        image_urls=response.xpath('//div[@class="img-box gif"]/img/@src').getall()
        name=response.xpath('//div[@class="img-box gif"]/img/@title').get()

        item=Gif588KuItem(image_urls=image_urls,name=name)
        # item['image_urls']=image_urls
        # item['name']=name
        yield item
