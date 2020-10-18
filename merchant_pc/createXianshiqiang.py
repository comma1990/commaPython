# Author ： comma
# 日期 : 2020/10/16  23:06

# 限时抢创建 url：https://www.shop2cn.com/service/mgmt/api/marketing/createEditPromotion
import requests
import urllib3
import json

def createXsq():
    from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    from merchant_pc.getTime import getAddMinutesTime2,getAddDaysTime2,getAddDaysTime3,getAddMinutesTime3
    beginTime=getAddMinutesTime3()
    endTime=getAddDaysTime3()
    promotionBeginTime=getAddMinutesTime2()
    promotionTimeEndTime=getAddDaysTime2()

    '''设置请求数据'''
    requestData = {"name": "py测试", "promotionTime": [promotionBeginTime, promotionTimeEndTime],
                   "limitType": 1, "limitNum": "", "previewTime": 0, "preTime": "",
                   "beginTime": beginTime, "endTime": endTime,
                   "productList": [{"productId": "p7084378", "catalogList":
                       [{"catalogId": "c43699135", "buyingPrice": 0, "salePrice": 0.1, "stockNum": 100, "realStock": 100,
                         "virtualStock": 0, "propertyValue": "白色", "sku": None, "barcode": None, "counterPrice": 0,
                         "marketAmount": 0, "activityRealStock": 0, "activityStock": 0, "discount": "5.6",
                         "discountPrice": "0.06"},
                        {"catalogId": "c43699134", "buyingPrice": 0, "salePrice": 0.2, "stockNum": 200,
                         "realStock": 200, "virtualStock": 0, "propertyValue": "黑色", "sku": None, "barcode": None,
                         "counterPrice": 0, "marketAmount": 0, "activityRealStock": 0, "activityStock": 0,
                         "discount": "5.6", "discountPrice": "0.11"}]},
                                   {"productId": "p7084377", "catalogList": [
                                       {"catalogId": "c43698270", "buyingPrice": 0, "salePrice": 0.1, "stockNum": 100,
                                        "realStock": 100, "virtualStock": 0, "propertyValue": "白色", "sku": None,
                                        "barcode": None, "counterPrice": 0, "marketAmount": 0, "activityRealStock": 0,
                                        "activityStock": 0, "discount": "5.6", "discountPrice": "0.06"},
                                       {"catalogId": "c43698269", "buyingPrice": 0, "salePrice": 0.2, "stockNum": 200,
                                        "realStock": 200, "virtualStock": 0, "propertyValue": "黑色", "sku": None,
                                        "barcode": None, "counterPrice": 0, "marketAmount": 0, "activityRealStock": 0,
                                        "activityStock": 0, "discount": "5.6", "discountPrice": "0.11"}]}],
                   "discountType": 0, "stockType": 0, "activityId": "", "activityType": 1, "sectionId": "4"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/mgmt/api/marketing/createEditPromotion', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    #depotId = json.loads(response)['data']['depotList'][1]['depotId']
    print(response)
    return response

if __name__ == '__main__':
    createXsq()