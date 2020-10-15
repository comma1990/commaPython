#author : comma
#date : 2020/10/15 15:513

# GET https://www.shop2cn.com/service/order/api/product/categories
# 获取全部分类信息
import requests
import urllib3
import json
import openpyxl

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

# 通过循环将分类信息打印到Excel表中
if __name__ == '__main__':
    wk=openpyxl.Workbook()
    sheet=wk.create_sheet('分类')
    sheet.append(['分类名称','分类id'])

    data=getCategories()
    for item in data:
        firChild=item['children']
        for sec in firChild:
            secChild=sec['children']
            for thirChild in secChild:
                name=thirChild['label']
                pid=thirChild['pid']
                sheet.append([name,pid])
    wk.save('/Users/sun/PycharmProjects/data/商品分类信息.xlsx')