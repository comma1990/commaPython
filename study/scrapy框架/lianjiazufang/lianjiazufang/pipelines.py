# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class LianjiazufangPipeline:
    def open_spider(self, spider):
        self.clien=MongoClient()
        self.zufang=self.clien.comma.lianjiazufang

    def process_item(self, item, spider):
        self.zufang.insert(dict(item))
        return item
    def close_spider(self, spider):
        self.clien.close()