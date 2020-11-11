# author : comma
# date : 2020/11/11 11:18

'''
待支付订单：https://www.shop2cn.com/service/order/api/orders/owner
{"orderStatus":1,"pageIndex":1,"pageSize":20,"placeOrderBeginTime":1573488000000,"placeOrderEndTime":1605110399999}

[data][proxyOrderList][0][orderId]       =1570212671

取消订单：https://www.shop2cn.com/service/order/api/order/cancel
{"orderId":1570202671,"cancelType":2}
'''
import json

import requests
import getCookie
import urllib3


def orderlist(pageindex): # 获取订单列表—— orderStatus：1待支付
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    Cookie = getCookie.getCookies()
    url = 'https://www.shop2cn.com/service/order/api/orders/owner'
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    requstData = {"orderStatus": 1, "pageIndex": pageindex, "pageSize": 20, "placeOrderBeginTime": 1573488000000,
                  "placeOrderEndTime": 1605110399999}
    urllib3.disable_warnings()
    data = requests.post(url, headers=headers, json=requstData, verify=False)
    # print(data.text)
    orderList = json.loads(data.text)['data']['proxyOrderList']
    # print(orderList)
    return orderList

def cancelOrder(orderid):   # 取消订单
    Cookie=getCookie.getCookies()
    url ='https://www.shop2cn.com/service/order/api/order/cancel'
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    requestData={"orderId":orderid,"cancelType":2}
    data=requests.post(url,headers=headers,json=requestData,verify=False)
    print(data.text)


if __name__ == '__main__':
    lst=orderlist(1)
    for item in lst:
        print(item['orderId'])
        cancelOrder(item['orderId'])

    #cancelOrder()