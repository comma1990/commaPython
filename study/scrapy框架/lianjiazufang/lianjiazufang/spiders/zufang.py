import scrapy


class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://sh.lianjia.com/zufang/pg{i}/#contentList' for i in range(1,3)]

    def parse(self, response):
        url_list=['https://sh.lianjia.com'+url for url in response.xpath('//div[@class="content__list--item--main"]/p[1]/a/@href').getall()]
        # print(url_list)
        for item in url_list:
            yield scrapy.Request(url=item,callback=self.parse_info)

    def parse_info(self,response):
        name=response.xpath('//div[@class="content clear w1150"]/p/text()').get() #名称
        price=response.xpath('//div[@class="content__aside--title"]/span/text() | //div[@class="content__aside--title"]/text()').getall() #价格
        price=''.join(price).strip().replace('\n            ','')
        rent_type=response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get()#租赁方式：整租，合租
        house_type=response.xpath('//ul[@class="content__aside__list"]/li[2]/text()').get()#房屋类型，几室几厅
        floor=response.xpath('//li[@class="floor"]/span/text()').getall() #楼层信息
        floor=''.join(floor)
        area=response.xpath('//div[@id="info"]/ul/li[2]/text()').get()#面积
        direction=response.xpath('//div[@id="info"]/ul/li[3]/text()').get() #朝向
        elevator=response.xpath('//div[@id="info"]/ul/li[9]/text()').get()# 电梯
        gas = response.xpath('//div[@id="info"]/ul/li[15]/text()').get()  # 燃气

        yield {
            'name':name,
            'price':price,
            'rent_type':rent_type,
            'house_type':house_type,
            'floor':floor,
            'area':area,
            'direction':direction,
            'elevator':elevator,
            'gas':gas



        }





