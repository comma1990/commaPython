# author : comma
# date : 2020/12/2 10:26
'''
https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17104536339297060099_1606875519516&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1606875613014
去掉地址中：jsoncallback=jQuery17104536339297060099_1606875519516&，返回的结果就是json格式了

图片地址：sProdImgNo_8: "http%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735120117%2F1606814547%5F84828260%5F690%5FsProdImgNo%5F8%2Ejpg%2F200"

'''
import requests
import time
import json
import urllib3
import urllib.parse
import os
from urllib import request


def wangzhewallpaper(pageid):
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Referer': 'https: // pvp.qq.com /'
               }
    url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={pageid}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1606875613014'
    urllib3.disable_warnings()
    responsedata = requests.get(url, headers=headers, verify=False)
    # json_data=responsedata.text.replace('jQuery17104536339297060099_1606875519516(','').replace(')','') # replace替换
    # print(responsedata.text)
    # wallpaper_list=json.loads(responsedata.text)['List']
    wallpaper_list=responsedata.json()['List']
    # print(gaoqing_list)
    return wallpaper_list



def save():
    d={}
    wallpaper_list = wangzhewallpaper(0)
    for item in wallpaper_list:
        pic_url=urllib.parse.unquote(item['sProdImgNo_8']).replace('200','0')
        pic_name=urllib.parse.unquote(item['sProdName'])
        d[pic_name]=pic_url
        # print(pic_url,pic_name)
    for item in d:
        dirpath=os.path.join('D:\素材\王者荣耀',item) # 拼接路径
        os.mkdir(dirpath)   # 创建文件夹
        request.urlretrieve(d[item],os.path.join(dirpath,'{}.jpg').format(item))
        print(item,'下载完成')
        # print(item,d[item])

def save2():
    for i in range(23):
        wallpaper_list=wangzhewallpaper(i)
        for item in wallpaper_list:
            pic_url = urllib.parse.unquote(item['sProdImgNo_8']).replace('200', '0')
            pic_name = urllib.parse.unquote(item['sProdName'])
            request.urlretrieve(pic_url,os.path.join('D:\素材\王者荣耀',f'{pic_name}.jpg'))
            print(pic_name,'下载完成')
    time.sleep(2)



if __name__ == '__main__':
    # wangzhewallpaper()
    # save()
    save2()
