#author : comma
#date : 2020/12/1 13:51
'''
www.shop2cn.com	/service/order/api/product/categories
'''
import requests
import urllib3
import json
import random
def getcategories(Cookie):
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Cookie':Cookie
               }
    urllib3.disable_warnings()
    responsedata=requests.get('https://www.shop2cn.com/service/order/api/product/categories',headers=headers,verify=False)
    # print(responsedata.text)
    data=json.loads(responsedata.text)['data']['list']
    x=random.randint(0,25)
    leve1=data[x]
    leve1_value=leve1['value']
    leve2=leve1['children'][0]
    leve2_value=leve2['value']
    leve3=leve2['children'][0]
    leve3_value=leve3['value']
    return leve1_value,leve2_value,leve3_value


if __name__ == '__main__':
    from merchant_pc import getCookie
    Cookie=getCookie.getCookies()
    result=getcategories(Cookie)
    print(type(result))
    print(result)
    print(result[1])