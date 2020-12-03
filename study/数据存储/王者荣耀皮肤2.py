# @Author  :  comma 
# @Date    :  2020-12-02 22:23

import requests
import time
import urllib.parse
from urllib import request
import os


def send_request(pageid):
    url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={pageid}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1606919172579'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'referer': 'https://pvp.qq.com/web201605/wallpaper.shtml'}
    responsedata = requests.get(url, headers=headers)
    return responsedata.json()
    # print(responsedata.text)


def get_url(data):
    image_url_list = []
    for i in range(1, 9):
        image_url = urllib.parse.unquote(data['sProdImgNo_{}'.format(i)]).replace('200', '0')
        image_url_list.append(image_url)
    return image_url_list


def parse_json(json_data):
    d = {}
    data_list = json_data['List']
    for data in data_list:
        image_url_list = get_url(data)
        sProdName = urllib.parse.unquote(data['sProdName'])
        d[sProdName] = image_url_list
    # for item in d:
    #     print(item, d[item])
    save_jpg(d)


def save_jpg(d):
    for key in d:
        dirpath=os.path.join('/Users/sun/Downloads/王者荣耀皮肤',key).strip(' ') # 拼接路径
        os.mkdir(dirpath) # 创建文件夹
        # 下载图片并保存
        for index,image_url in enumerate(d[key]):
            request.urlretrieve(image_url,os.path.join(dirpath,'{}.jpg'.format(index+1)))
            print(key,d[key][index],'下载完成')


def start():
    for i in range(3,20):
        json_data = send_request(i)
        parse_json(json_data)
        time.sleep(5) #不睡眠的话会被禁止访问


if __name__ == '__main__':
    start()
