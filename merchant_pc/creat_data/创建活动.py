# Author ： comma
# 日期 : 2020/10/17  10:14

# 创建活动
'''流程——①先获得商品列表输出到Excel表中getProductId
        ②从商品列表中获取没有活动信息的商品getgetNoActivityProductId-----（调用了获取商品活动信息的方法getPoductActivityInfo）
        ③向每个规格中添加活动信息，作为活动商品数据'''
'''商品参数信息
{"productId": "p7084378", "catalogList":[{"catalogId": 。。。。}]}
'''
import requests
import urllib3
import random
import datetime


def createXsq(Cookie, productList, sectionType, sectionId):  # sectionType 1-限时抢，2-秒杀
    # from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    from merchant_pc.getTime import getAddMinutesTime2, getAddDaysTime2, getAddMinutesTime, getAddMinutesTime3,getAdd2MinutesTime
    beginTime = getAddMinutesTime()
    endTime = getAddDaysTime2()
    promotionBeginTime = getAddMinutesTime()
    promotionTimeEndTime = getAddDaysTime2()

    '''设置请求数据
    限时抢：activityType=1，sectionId=4
    秒杀：activityType=2，sectionId=5'''
    # x=random.randint(1,100) # 定义一个随机数用于创建活动名称使用
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M')  # 获取当前时间用作创建活动名称使用
    requestData = {"name": f"限时抢{date}号", "promotionTime": [promotionBeginTime, promotionTimeEndTime],
                   "limitType": 1, "limitNum": "", "previewTime": 0, "preTime": "",
                   "beginTime": beginTime, "endTime": endTime,
                   "productList": productList,
                   "discountType": 0, "stockType": 0, "activityId": "", "activityType": sectionType,
                   "sectionId": sectionId}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/mgmt/api/marketing/createEditPromotion', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)
    # return response


if __name__ == '__main__':
    from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie

    Cookie = getCookies()
    productList = []  # 定义一个空列表接收商品id和规格信息
    x = 0  # 计数器
    sellerid = eval(input('请输入商户id：'))  # 商户id，查询商品信息需要   500002398，500041475   国内渠道商：500021576
    # print('请先确认sellerID是否正确！！！筛选商品需要用到')
    sectionType = eval(input('你想创建限时抢还是秒杀，1-限时抢，2-秒杀：'))
    n = int(input('请输入你想添加的商品个数：'))
    discount = eval(input('请输入折扣：'))  # 设置折扣
    # 遍历商品列表，并在商品规格上添加活动库存信息
    from merchant_pc.getProduceList import getPorduceList  # 获取商品列表（创建活动时拉取的列表）

    pageindex = 5
    i = 1
    while i < pageindex:
        for item in getPorduceList(Cookie, i):  # 遍历商品列表
            productid = [item['id']]
            dic = {}  # 定义一个字典接收商品id和规格信息，将字典添加到列表中
            cateloglist = []  # 定义一个空规格列表，接收规格信息
            from merchant_pc.getPoductActivityInfo import getPoductActivityInfo

            if bool(getPoductActivityInfo(sellerid, productid)) == False:  # 判断商品没有活动信息后，添加规格的活动信息
                for catlog in item['catalogList']:  # 遍历规格列表
                    # cateloglist = []  # 定义一个空规格列表，接收规格信息
                    catlog['activityRealStock'] = 0  # 添加活动真实库存
                    catlog['activityStock'] = 0  # 添加活动库存 ——为0的时候默认使用全部库存
                    catlog['discount'] = discount  # 添加折扣信息
                    catlog['discountPrice'] = catlog['salePrice'] * discount / 10  # 添加折后价格
                    cateloglist.append(catlog)
                dic['productId'] = item['id']
                dic['catalogList'] = cateloglist
                x += 1
                if x > n:
                    break
                productList.append(dic)
        i += 1

        # print(productList)
    from merchant_pc.getSectionList import getSectionList

    sectionId = getSectionList(Cookie, sectionType)[0]['sectionId']
    createXsq(Cookie, productList, sectionType, sectionId)
