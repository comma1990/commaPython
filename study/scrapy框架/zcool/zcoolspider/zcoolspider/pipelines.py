# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from zcoolspider import settings
import os

class ZcoolspiderPipeline(ImagesPipeline):#自定义用于下载图片的pipeline



    #重写发送请求
    def get_media_requests(self, item, info):
        image_requests=super().get_media_requests(item,info)#获取图片链接请求的列表
        for img_req in image_requests:
            img_req.item=item #对每一个图片的连接请求都添加一个item属性
        return image_requests


        # urls = ItemAdapter(item).get(self.images_urls_field, [])
        # return [Request(u) for u in urls]




    #重写保存地址的方法，改变存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        old_path=super().file_path(request,response,info) #父类方法返回return f'full/{image_guid}.jpg'
        title=request.item['title'] # 获取图片标题
        # print(title)
        save_path=os.path.join(settings.IMAGES_STORE,title)
        #原路径中提取文件名
        image_name=old_path.replace('full/','')
        return os.path.join(title,image_name)



    # def process_item(self, item, spider):
    #     return item
