import requests
import urllib3
import random

'''创建商品'''


def createProduct():
    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    from merchant_pc.getDepot import getDepot
    depotId=getDepot()
   # loginId = 'gjgly' + str(x)
    title = 'python商品' + str(x)+'号'
    '''设置角色id——templateId'''
    requestData = {"saleType": 1, "source": "pc", "noReasonReturn": 1,
                   "currency": "CNY", "depotId": depotId, "subType": 1, "title": title, "subTitle": "副标题",
                   "categoryId": 1087, "thirdCategoryId": 1088, "category": [1086, 1087, 1088],
                   "pics": ["http://pic1.shop2cn.com/G03/M06/DF/E5/CgzUIV-FLdiAIgByAAENpCaDBHw074_1_1_n_x_o.jpg"],
                   "brandId": 10160, "marketCurrency": "JPY", "setAgentPrice": 0,
                   "catalogList": [{"directPrice": "0.1", "propertyValue": "白色", "pic": None,
                                    "catalogId": None, "parentCatalogId": None, "limitNum": 0, "marketPrice": None,
                                    "virtualStock": None, "marketAmount": 0, "stock": "100", "sku": None,
                                    "barcode": None,
                                    "propertyList": [{"name": "颜色", "value": "白色"}],
                                    "agentPriceList": [{"agentPrice": None, "agentTypeId": 28}]},
                                   {"directPrice": "0.2", "propertyValue": "黑色", "pic": None, "catalogId": None,
                                    "parentCatalogId": None, "limitNum": 0, "marketPrice": None, "virtualStock": None,
                                    "marketAmount": 0, "stock": "200", "sku": None, "barcode": None,
                                    "propertyList": [{"name": "颜色", "value": "黑色"}],
                                    "agentPriceList": [{"agentPrice": None, "agentTypeId": 28}]}],
                   "expressDelivery": 1, "collectionGoods": None, "catalogStatus": 101, "cardInfo": 1}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/product/publish', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)
