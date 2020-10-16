# Author ： comma
# 日期 : 2020/10/15  23:18
# GET https://www.shop2cn.com/service/order/api/product/brands?searchKey=l
# 获取品牌信息
import requests
import urllib3
import json
import openpyxl


def getBrands(i):
    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    url = 'https://www.shop2cn.com/service/order/api/product/brands?searchKey=' + str(i)
    urllib3.disable_warnings()
    data = requests.get(url, headers=headers, verify=False)
    response = data.text
    bransList = json.loads(response)['data']['list']
    #print(bransList)
    return bransList


if __name__ == '__main__':
    #getBrands('a')
    #print(getBrands('b'))

    wk=openpyxl.Workbook()
    sheet=wk.create_sheet('品牌')
    sheet.append(['名字','品牌id'])

    for item in range(26):
        brandList=getBrands(chr(item+ord('A')))      # ord('a')将字母a转成数字
        #print(brandList)
        for brand in brandList:
            if brandList !=None:
                name=brand['name']
                id=brand['id']
                sheet.append([name,id])
    wk.save('D:\python\study\品牌信息表.xlsx')
