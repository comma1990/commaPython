# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class DoubanPipeline:
    def __init__(self): #初始化用来创建工作簿对象
        self.wb=openpyxl.Workbook()
        self.sheet=self.wb.active
        self.sheet.append(['名称','出版信息','评分'])

    def process_item(self, item, spider):# item是一个类似于字典的数据
        # 根据键获取值
        line=[item['title'],item['publish'],item['score']]#根据键获取值，放入列表中
        #将列表的数据添加到工作表中
        self.sheet.append(line)
        return item


    #定义一个关闭的方法
    def close_spider(self,spider):
        self.wb.save('豆瓣图书top250.xlsx')
        self.wb.close()