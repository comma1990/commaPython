# author : comma
# date : 2020/10/14 14:28

# 将商品id保存到excel表中
import requests
import urllib3
import json
import openpyxl


def getProductId():
    wk = openpyxl.Workbook()
    sheet = wk.create_sheet()
    sheet.append(['productId','商品名称','品牌id','品牌名','分类id','分类'])

    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    # 设置请求数据
    requestData = {"pageIndex": 1, "pageSize": 100}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/product/list', json=requestData,
                         headers=headers,
                         verify=False)
    response = json.loads(data.text)
    productList=response['data']['productList']
   # print(response)
    for item in productList:
        productId=item['productId']
        productName=item['title']
        brandId = item['brandId']
        brandName=item['brandName']
        categoryId = item['categoryId']
        categoryName = item['categoryName']
        sheet.append([productId,productName,brandId,brandName,categoryId,categoryName])
        wk.save('/Users/sun/PycharmProjects/商品信息.xlsx')
    print('输出完毕！')
if __name__ == '__main__':
    getProductId()
