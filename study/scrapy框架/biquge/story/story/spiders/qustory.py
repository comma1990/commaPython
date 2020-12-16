import scrapy


class QustorySpider(scrapy.Spider):
    name = 'qustory'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/13/13959/5939025.html']

    def parse(self, response):
        #解析提取数据
        title=response.xpath('//h1/text()').extract()
        content=response.xpath('//div[@id="content"]/text()').extract_all()
        print(title,content)
