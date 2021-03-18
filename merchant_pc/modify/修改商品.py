#author : comma
#date : 2021/3/17 15:35
'''
 单规格商品修改
'''
import requests
import json
import urllib3
import getCookie

def modifyproduct(Cookie,productId):
    url='https://www.shop2cn.com/service/order/api/product/modifyProduct'
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Cookie': Cookie
               }
    requestdata={"saleType":0,"source":"pc","noReasonReturn":True,"role":1,"currency":"CNY","subType":1,"categoryId":1369,"thirdCategoryId":1370,"category":[1368,1369,1370],
                 "pointsGive":False,"pointsDeduction":True,"title":"排序","rate":1,"pics":["http://pic1.shop2cn.com/G03/M09/4B/B7/CgzUH2A2BJiAPwW1AAJVwSJo6d8437_900_871_n_x_o.jpg"],"marketCurrency":"JPY",
                 "catalogList":[{"directPrice":100,"marketAmount":0,"catalogId":"c60002889"}],
                 "setAgentPrice":False,"expressDelivery":True,"collectionGoods":False,"catalogStatus":1,"cardInfo":0,"description":None,"productId":productId,"saleArea":1}
    urllib3.disable_warnings()
    responsedata=requests.post(url,json=requestdata,headers=headers,verify=False)
    data=responsedata.text
    print(data)

if __name__ == '__main__':
    productId=input('请输入商品Id：')
    Cookie = getCookie.getCookies()
    modifyproduct(Cookie,productId)