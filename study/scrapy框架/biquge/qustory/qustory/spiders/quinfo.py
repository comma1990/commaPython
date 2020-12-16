import scrapy


class QuinfoSpider(scrapy.Spider):
    name = 'quinfo'
    allowed_domains = ['biquge.info']
    start_urls = ['http://www.biquge.info/0_383/1596644.html']

    def parse(self, response):
        title=response.xpath('//h1/text()').extract()
        content=response.xpath('string(//div[@id="content"])').extract_first().strip()
        yield {
            'title':title,
            'content':content
        }
        # print(title,content)
