# @Author  :  comma 
# @Date    :  2020-12-03 22:26


import requests
from urllib import request
from urllib import parse
import threading
from queue import Queue
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'referer': 'https://pvp.qq.com/web201605/wallpaper.shtml'}


def get_url(data):  # 获取图片地址，放入到列表中
    image_url_list = []
    for i in range(1, 9):
        image_url = parse.unquote(data['sProdImgNo_{}'.format(i)]).replace('200', '0')
        image_url_list.append(image_url)
    return image_url_list


# 生产者线程
class Producer(threading.Thread):
    def __init__(self, page_queue, image_url_queue):
        super().__init__()  # 调用父类的init方法
        self.page_queue = page_queue  # 给属性赋值
        self.image_url_queue = image_url_queue

    def run(self):
        while not self.page_queue.empty():  # 判断队列是否为空
            page_url = self.page_queue.get()  # 获取队列中的值，page_queue队列就是放页面地址的
            responsedata = requests.get(page_url, headers=headers)  # 获取请求结果
            json_data = responsedata.json()  # 请求结果转换成json格式
            # 解析数据，并将图片名字和图片url的列表放入到字典中
            d = {}
            data_list = json_data['List']
            for data in data_list:
                image_url_list = get_url(data)
                sProdName = parse.unquote(data['sProdName'])
                d[sProdName] = image_url_list
            # 遍历字典，以图片名称创建文件夹，并遍历每个列表中的图片的url放入到图片url队里里（image_url_queue）
            for key in d:
                dirpath = os.path.join('/Users/sun/Downloads/王者荣耀皮肤',
                                       key.strip(' ').replace('·', '').replace('1:1', ''))  # 拼接路径
                # 因为是多线程，所以需要先判断文件夹是否已经存在
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)  # 创建文件夹
                # 遍历图片列表，将图片url和存放图片的路径，放入到图片url队列里
                for index, image_url in enumerate(d[key]):
                    self.image_url_queue.put(
                        {'image_path': os.path.join(dirpath, f'{index + 1}.jpg'), 'image_url': image_url})


# 消费者线程
class Customer(threading.Thread):
    def __init__(self, image_url_queue):
        super().__init__()
        self.image_url_queue = image_url_queue

    def run(self):
        while True:
            try:
                image = self.image_url_queue.get(timeout=30)  # 从队列中获取图片对象,设置超时时间，当30s后还没有从线程中取到数据则抛一场，被Except捕获后退出
                request.urlretrieve(image['image_url'], image['image_path'])
                print(image['image_path'], '下载完成')
            except:
                break


# 定义一个启动线程的函数
def start():
    page_queue = Queue(23)  # 定义一个获取页面链接的线程，线程数是23，有23页皮肤
    image_url_queue = Queue(1000)  # 定义一个获取图片url的线程，线程数为1000
    for pageid in range(23):
        page_url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={pageid}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1606919172579'
        # print(page_url)
        page_queue.put(page_url)  # 将页面的url放入线程队列中

    # 创建生产者线程对象
    for i in range(5):
        t = Producer(page_queue, image_url_queue)  # 生产者需要从队列中获取页面的url（page_queue），并将获取的图片url放入到队列中（image_url_queue）
        t.start()

    # 创建消费者线程对象
    for i in range(10):
        t = Customer(image_url_queue)  # 消费者线程需要从队列中获取图片的url（image_url_queue）
        t.start()


if __name__ == '__main__':
    start()
