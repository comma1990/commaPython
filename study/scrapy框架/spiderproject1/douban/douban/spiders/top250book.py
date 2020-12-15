# @Author  :  comma 
# @Date    :  2020-12-14 21:34


import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem


class DoubanScrapy(scrapy.Spider):  # 继承scrapy的爬虫类
    name = 'douban'
    allowed_domain = ['book.douban.com/top250']  # 定义运行爬虫爬取的域名
    start_urls = ['https://book.douban.com/top250']  # 定义起始网址，告诉爬虫程序应该从哪个网址开始爬取

    # parse是scrapy框架里默认处理response（响应）的一个方法
    def parse(self, response):
        # print(response.text)
        bs = BeautifulSoup(response.text, 'lxml')
        tr_tag = bs.find_all('tr', class_='item')
        for tr in tr_tag:
            item=DoubanItem()
            title = tr.find_all('a')[1]['title']  # 提取书名
            publish=tr.find('p',class_='pl').text # 提取出版信息
            score=tr.find('span',class_='rating_nums').text #提取评分
            # # 测试打印
            print([title, publish, score])

            #将数据赋值个item对象的属性
            item['title']=title
            item['publish']=publish
            item['score']=score

            #数据封装完毕后，需要提交给引擎
            yield item

