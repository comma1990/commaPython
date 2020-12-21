import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZcoolspiderItem


class ZcoolSpider(CrawlSpider):
    name = 'zcool'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/?p=1#tab_anchor']

    rules = (
        Rule(LinkExtractor(allow=r'/?p=\d+#tab_anchor'),  follow=True),
        Rule(LinkExtractor(allow=r'/work/.+=.html'), callback='parse_item', follow=False),

    )

    def parse_item(self, response):
        img_urls=response.xpath('//div[@class="photo-information-content"]/img/@src').getall()
        title=response.xpath('//h2/text()').getall()
        title=''.join(title).strip()

        item=ZcoolspiderItem(image_urls=img_urls,title=title)
        yield item
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
