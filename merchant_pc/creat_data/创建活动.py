# Author ： comma
# 日期 : 2020/10/17  10:14

# 创建活动
'''流程——①先获得商品列表输出到Excel表中getProductId
        ②从商品列表中获取没有活动信息的商品getgetNoActivityProductId-----（调用了获取商品活动信息的方法getPoductActivityInfo）
        ③向每个规格中添加活动信息，作为活动商品数据'''
'''商品参数信息
{"productId": "p7084378", "catalogList":
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
                                        "activityStock": 0, "discount": "5.6", "discountPrice": "0.11"}]}
'''
import requests
import urllib3
import json
import openpyxl
import xlrd

def createXsq(productList):
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
                   "productList": productList,
                   "discountType": 0, "stockType": 0, "activityId": "", "activityType": 1, "sectionId": "4"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/mgmt/api/marketing/createEditPromotion', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    #depotId = json.loads(response)['data']['depotList'][1]['depotId']
    print(response)
    #return response

if __name__ == '__main__':
    # wk=openpyxl.Workbook()
    # sheet=wk.create_sheet('活动商品列表')
    productList=[]  #定义一个空列表接收商品id和规格信息
    dic={}  #定义一个字典接收商品id和规格信息，将字典添加到列表中
    x=0     # 计数器
    sellerid=500002398 #商户id，查询商品信息需要
    n=int(input('请输入你想添加的商品个数：'))
    #discount = 5.6  # 设置折扣
    discount=int(input('请输入折扣：'))
    # 遍历商品列表，并在商品规格上添加活动库存信息
    from merchant_pc.getProduceList import getPorduceList   #获取商品列表（创建活动时拉取的列表）
    for item in getPorduceList(2):   #遍历商品列表
        from merchant_pc.getPoductActivityInfo import getPoductActivityInfo
        if bool(getPoductActivityInfo(sellerid,item['id']))==False:     #判断商品没有活动信息后，添加规格的活动信息，并添加到Excel表中
            for catlog in item['catalogList']:  #遍历规格列表
                catlog['activityRealStock']=0    #添加活动真实库存
                catlog['activityStock']=0    # 添加活动库存 ——为0的时候默认使用全部库存
                catlog['discount']=discount     # 添加折扣信息
                catlog['discountPrice']=catlog['salePrice']*discount/10   # 添加折后价格
                dic['productId']=item['id']
                dic['catalogList']=catlog
                productList.append(dic)
                x+=1
                if x>n:
                    break
    createXsq(productList)
                # sheet.append([item['id'],str(catlog).replace('\'','"')])
    wk.save('D:\python\study\活动商品列表.xlsx')
    # 表中的数据都是添加好活动信息的，现在需要提取出来，id和category组合作为请求参数