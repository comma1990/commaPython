import requests
import urllib3
import random
import xlrd

'''创建商品'''


#   getCookie方法提取到公共方法中，调用改方法必须先传cookie


def createProduct(Cookie,
                  pic):  # 商品图片["http://pic1.shop2cn.com/G03/M06/DF/E5/CgzUIV-FLdiAIgByAAENpCaDBHw074_1_1_n_x_o.jpg"]
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    # from merchant_pc.getDepot import getDepot
    # depotId = getDepot(Cookie)
    # loginId = 'gjgly' + str(x)
    title = 'python商品' + str(x) + '号'
    '''设置角色id——templateId'''
    requestData = {"saleType": 1, "source": "pc", "noReasonReturn": 1,
                   "currency": "CNY", "depotId": 0, "subType": 1, "title": title, "subTitle": "副标题",
                   "categoryId": 1087, "thirdCategoryId": 1088, "category": [1086, 1087, 1088],
                   "pics": pic,
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

if __name__ == '__main__':
    from merchant_pc import getCookie
    Cookie=getCookie.getCookies()
    '''创建商品,循环创建'''
    wk = xlrd.open_workbook('D:\python\study\中免商品信息.xlsx')
    sheet = wk.sheets()[1]
    x = int(input('请输入你想从第几张图片开始创建商品：'))
    if x>sheet.nrows:
        print('商品图片数量不足！！！')
    else:
        n = int(input('请输入要创建的商品数量：'))
        if n > sheet.nrows - x:
            print('商品图片数量不足！')
        else:
            for item in range(n):
                pic = sheet.col_values(6, x, x + 1)     # 从表中索引为6列取值，值的返回是x行到x+1行
                createProduct(Cookie, pic)
                x += 1
