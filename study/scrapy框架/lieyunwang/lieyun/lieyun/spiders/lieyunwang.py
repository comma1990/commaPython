import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LieyunItem



class LieyunwangSpider(CrawlSpider):
    name = 'lieyunwang'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['http://lieyunwang.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/latest/p\d+.html'), follow=True),  # \d+ 正则表达式 \d匹配数字 +一次或多次
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback='parse_item', follow=False),

    )

    def parse_item(self, response):
        title_list = response.xpath('//h1[@class="lyw-article-title-inner"]/text()').getall()
        title = ''.join(title_list).strip()  # 标题
        publish_date = response.xpath('//span[@class="time"]/text()').get()  # 发布时间
        author = response.xpath('//a[contains(@class,"author-name")]/text()').get()  # 作者
        # author=response.xpath('//a[@class="author-name open_reporter_box"]/text()').get()
        content = response.xpath('//div[@class="main-text"]//text()').getall()
        content = ''.join(content).strip()
        article_url=response.url
        # print(title, publish_date, author)

        #创建Item对象
        item=LieyunItem()
        item['title']=title
        item['publish_date']=publish_date
        item['author']=author
        item['content']=content
        item['article_url']=article_url

        yield item

        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        # print(response.url)
