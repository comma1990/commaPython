# Author ： comma
# 日期 : 2020/10/16  23:42

# 获取商品列表：https://www.shop2cn.com/service/mgmt/api/page/produceList?status=1&pageIndex=1&pageSize=20
import requests
import urllib3
import json
import openpyxl

def getPorductList(pageIndex): # pageIndex页码，你想获得哪页的数据
    from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    Cookie = getCookies()
    #text/html,application/xhtml+xml,application/xml
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng, */*',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    #json=requestData,?status=1&pageIndex=1&pageSize=20
    #requestData = {"status": 1,"pageIndex":int(pageIndex), "pageSize": 100},json=requestData,
    urllib3.disable_warnings()
    data = requests.get(f'https://www.shop2cn.com/service/mgmt/api/page/produceList?status=1&pageIndex={pageIndex}&pageSize=20',
                         headers=headers,
                         verify=False)
    response = data.text
    productList=json.loads(response)['data']['productList']
    return productList

if __name__ == '__main__':
    # 遍历商品列表，并在商品规格上添加活动库存信息
    for item in getPorductList(2):   #遍历商品列表
        for catlog in item['catalogList']:  #遍历规格列表
            catlog['activityRealStock']=0    #添加活动真实库存
            catlog['activityStock']=0    # 添加活动库存 ——为0的时候默认使用全部库存
        print(catlog)