import requests
import urllib3
import random
import xlrd
import time

def createCoupon(productIdList):
    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    x=random.randint(100,200)
    name='Python优惠券'+str(x)
    #recTime=time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime()) #"2020-10-24T23:59:59"
    #effTime=time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())
    from merchant_pc.getTime import getAddMinutesTime,getAddDaysTime
    recTime=getAddMinutesTime()
    effTime=getAddMinutesTime()
    recEndTime=getAddDaysTime()
    effEndTime=getAddDaysTime()
    #orderMinAmount——满足的金额，couponAmount——优惠券的金额
    #productIdList适用商品列表,["p5985277","p5985276","p5985275","p5985274"]
    requestData = {"batchName":name,"acquireStartTime":recTime,
                   "acquireEndTime":recEndTime,"effectiveStartDate":effTime,
                   "effectiveEndDate":effEndTime,"orderMinAmount":"20","couponAmount":"10",
                   "couponTotalCount":"100","receiveNumPerUser":"5","useConditionType":2,
                   "productIdList":productIdList,"currency":"CNY","isShowInPage":1}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/marketing/api/yhq/create', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)
if __name__ == '__main__':
    wk=xlrd.open_workbook('/Users/sun/PycharmProjects/商品信息.xlsx')
    data=wk.sheets()[1]
    # 想要创建几张优惠券range后的数字就填几
    for i in range(5):
        if i != 0:
            pls = data.col_values(0, i, i + 3)  # 读去第0列，第i行到第i+3行数据
            i += 3
            #nn = str(pls).replace("'", "")
            #print(productplIdList)
            createCoupon(pls)

    #createCoupon(),productplIdList