import scrapy
from scrapy import signals
from selenium.webdriver import Chrome

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaiduSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.driver=Chrome() # 创建完爬虫对象，给爬虫添加浏览器对象属性
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider


    def spider_closed(self, spider):
        # 关闭浏览器对象
        spider.driver.close()

        #spider.logger.info('Spider closed: %s', spider.name)

    def parse(self, response):
        print(response.text)
