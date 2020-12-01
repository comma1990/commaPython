# author : comma
# date : 2020/12/1 16:43

'''
https://www.shop2cn.com/service/order/api/product/brands?searchKey=b
'''
import requests
import json
import urllib3
import random


def getbrands(Cookie, key):
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Cookie': Cookie
               }
    url = f'https://www.shop2cn.com/service/order/api/product/brands?searchKey={key}'
    urllib3.disable_warnings()
    responsedata = requests.get(url, headers=headers, verify=False)
    data = json.loads(responsedata.text)['data']['list']
    # print(data)
    return data


def getrandombrand(Cookie):
    m = random.randint(0, 26)
    key = chr(ord('a') + m)
    brands = getbrands(Cookie, key)
    l = len(brands)
    n = random.randint(0, l-1)
    brandId = brands[n]['id']
    return brandId


if __name__ == '__main__':
    from merchant_pc import getCookie

    Cookie = getCookie.getCookies()
    # for i in range(26):
    #     key=(chr(ord('a')+i))
    #     getbrands(Cookie,key)
    x = getrandombrand(Cookie)
    print(x)
