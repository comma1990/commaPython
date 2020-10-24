# Author ： comma
# 日期 : 2020/10/16  22:04

# 获取商品活动信息

import requests
import urllib3
import json


def getPoductActivityInfo(sellerId,productId):  # productId ["p4740703", "p4740702", "p4706337", "p4740694"]
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Connection': 'keep - alive',
               }
    '''设置请求数据'''
    requestdata = {
        "sellerId": sellerId,
        "productIds": productId
    }
    urllib3.disable_warnings()
    data = requests.post('http://shopbiz.iapi.ymatou.com/api/page/getDiscountProductList',
                         json=requestdata,
                         headers=headers,
                         verify=False)
    response = data.text
    acticityInfo = json.loads(response)['data']['productList']  # productlist为空的时候表明商品没有活动
    print(response)
    return acticityInfo


if __name__ == '__main__':
    productlist=['p5985269']
    sellerid=500002398
    result=getPoductActivityInfo(sellerid,productlist)
    print(result)
