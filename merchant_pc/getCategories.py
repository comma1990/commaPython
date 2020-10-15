#author : comma
#date : 2020/10/15 15:513

# GET https://www.shop2cn.com/service/order/api/product/categories
# 获取全部分类信息
import requests
import urllib3
import json

def getCategories():
    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    urllib3.disable_warnings()
    data = requests.get('https://www.shop2cn.com/service/order/api/product/categories',
                          headers=headers,
                          verify=False)
    response = data.text
    categories=json.loads(response)['data']['list']#[0]['children'][0]['label']
    return categories
    #print(categories)

if __name__ == '__main__':
    data=getCategories()
    for item in data:
        secChild=item[0]
        for sc in secChild:
            for thirChild in sc['children']:
                for last in thirChild[]:
                    for lastChild