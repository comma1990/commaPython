# Author ： comma
# 日期 : 2020/10/16  22:04

# 获取商品活动信息

import requests
import urllib3
import json


def getPoductActivityInfo(sellerId, productId):  # productId ["p4740703", "p4740702", "p4706337", "p4740694"]
    '''设置请求数据'''
    requestdata = {
        "sellerId": sellerId,
        "productIds": productId
    }
    urllib3.disable_warnings()
    data = requests.post('http://shopbiz.iapi.ymatou.com/api/page/getDiscountProductList',
                         json=requestdata,
                         verify=False)
    response = data.text
    acticityInfo = json.loads(response)['data']['productList']  # productlist为空的时候表明商品没有活动
    # print(response)
    return acticityInfo


if __name__ == '__main__':
    productlist = ['p5985269']
    sellerid = 500002398
    result = getPoductActivityInfo(sellerid, productlist)
    print(result)
