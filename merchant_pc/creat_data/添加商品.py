#author : comma
#date : 2020/12/1 10:49
import requests
import urllib3
import random
import mysql.connector

def createProduct(Cookie,pic):  # pic的类型需要是一个列表
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Cookie':Cookie
               }
    x = random.randint(10, 50)  # 商品名称定义
    m = random.randint(10, 30)  # 规格1价格
    n = random.randint(30, 50)  # 规格2价格
    from merchant_pc.getDepot import getDepot
    depotId = getDepot(Cookie)  #获取仓库

    from get_data import getcategories  # 随机获取分类
    category = list(getcategories.getcategories(Cookie))
    categoryId = category[0]
    thirdCategoryId = category[2]

    from get_data import getbrands  # 随机获取一个品牌id
    brandId=getbrands.getrandombrand(Cookie)


    title = '不限境内外' + str(x) + '号'
    '''设置角色id——templateId'''
    requestData = {"saleType": 1, "source": "pc", "noReasonReturn": True,
                   "currency": "CNY", "depotId": depotId, "subType": 1, "title": title, "subTitle": "副标题",
                   "categoryId": categoryId, "thirdCategoryId": thirdCategoryId, "category": category,
                   "pics": pic,
                   "brandId": brandId, "marketCurrency": "JPY", "setAgentPrice": False,
                   "catalogList": [
                                   {"directPrice": n, "propertyValue": "黑色", "pic": None, "catalogId": None,
                                    "parentCatalogId": None, "limitNum": 0, "marketPrice": None, "virtualStock": None,
                                    "marketAmount": 0, "stock": "200", "sku": None, "barcode": None,
                                    "propertyList": [{"name": "颜色", "value": "黑色"}],
                                    "agentPriceList": [{"agentPrice": None, "agentTypeId": 28}]}],
                   "expressDelivery": 1, "collectionGoods": None, "catalogStatus": 101, "cardInfo": 1,'saleArea':3}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/product/publish', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)
def getpicurl(m,n):
    connector=mysql.connector.connect(host='localhost',user='root',passwd='root',database='haikun',auth_plugin='mysql_native_password')
    curcor=connector.cursor()
    sql='select picUrl from productpic LIMIT {},{}'.format(m,n)
    curcor.execute(sql)
    picurl_list =curcor.fetchall()
    return picurl_list

if __name__ == '__main__':
    from merchant_pc import getCookie
    Cookie=getCookie.getCookies()
    m=eval(input('请输入你想从第几张图片开始：'))
    n=eval(input('请输入你想创建商品的数量：'))
    picurl_list=getpicurl(m,n)  # 从第m张图片开始获取n张图片
    for item in picurl_list:    #遍历的元素是元组
        pic=list(item)
        createProduct(Cookie, pic)

