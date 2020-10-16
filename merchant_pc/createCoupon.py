import requests
import urllib3
import random

def createCoupon(Cookie):
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    x=random.randint(100,200)
    name='多品牌+多类目'#+str(x)
    # orderMinAmount——满足的金额，couponAmount——优惠券的金额
    # productIdList适用商品列表，全场通用则传null,指定商品["p5985277","p5985276","p5985275","p5985274"]
    # useConditionType：1全部商品，2.指定商品
    from merchant_pc.getTime import getAddDaysTime,getAddMinutesTime
    actStartTime=getAddMinutesTime()  #"2020-10-24T23:59:59"
    actEndTime=getAddDaysTime()
    effStartTime=getAddMinutesTime()
    effEndTime=getAddDaysTime()
    requestData = {"batchName":name,"acquireStartTime":actStartTime,
                   "acquireEndTime":actEndTime,"effectiveStartDate":effStartTime,
                   "effectiveEndDate":effEndTime,"orderMinAmount":"20","couponAmount":"10",
                   "couponTotalCount":"100","receiveNumPerUser":"5","useConditionType":1,
                   "productIdList":None,
                   "currency":"CNY","isShowInPage":1}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/marketing/api/yhq/create', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)

if __name__ == '__main__':
    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
    createCoupon(Cookie)