import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LiepinItem


class LiepinspiderSpider(CrawlSpider):
    name = 'liepinspider'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    rules = (
        Rule(LinkExtractor(allow=r'/job/\d+\.shtml.*'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/job/1934466825.shtml.*'), callback='parse_item', follow=False),

    )

    def parse_item(self, response):
        title=response.css('.title-info h1::text').get()
        company=response.css('.company-logo p a::text').get()

        # print(title)
        # print(response.xpath('//div[@class="job-info"]/h3/a/@href'))
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        item=LiepinItem(title=title,company=company)
        yield item

