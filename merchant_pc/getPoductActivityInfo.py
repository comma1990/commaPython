# Author ： comma
# 日期 : 2020/10/16  22:04

# 获取商品活动信息

import requests
import urllib3
import json


def getPoductActivityInfo(productId):  # productId ["p6400551"]
    from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''

    urllib3.disable_warnings()
    data = requests.get(f'http://productquery.iapi.shop2cn.com/api/Product/GetProductInfoByProductId?ProductId={productId}&NextActivityExpire=365',
                         headers=headers,
                         verify=False)
    response = data.text
    acticityInfo = json.loads(response)['Data']['Product']['ProductActivity']
    #print(acticityInfo)
    return acticityInfo


if __name__ == '__main__':
    getPoductActivityInfo('p5985269')
