# Author ： comma
# 日期 : 2020/10/16  22:04

# 商品详细信息
# url：http://productquery.iapi.ymatou.com/api/Product/GetProductDetailListByTradeIsolation
# ————————参数：————————————
#     {
#         "ProductIdList":["p6400551"],
#         "AppId":"evtadmin.ymatou.cn",
#         "NextActivityExpire":17
#     }
import requests
import urllib3
import json

# class ProductInfo():
#     # def __init__(self):
#     #     pass

def getPoductActivityInfo(productId):  # productId ["p6400551"]
    from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    requestData = {
        "ProductIdList": productId,
        "NextActivityExpire": 17
    }
    urllib3.disable_warnings()
    data = requests.post('http://productquery.iapi.shop2cn.com/api/Product/GetProductInfoByProductId',
                         json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    acticityInfo = json.loads(response)['data']
    print(response)
    if acticityInfo == None:
        return True
    else:
        return False
    # return productInfo


if __name__ == '__main__':
    getPoductActivityInfo("p6400551")
