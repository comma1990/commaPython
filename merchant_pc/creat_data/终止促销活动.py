#author : comma
#date : 2020/11/12 16:24
'''
get https://www.shop2cn.com/service/mgmt/api/marketing/queryPromotionList?page=1&pageSize=30&activityStatus=1&activityType=3
数据结构[data][records][0][activityId=500001410]

post  https://www.shop2cn.com/service/mgmt/api/marketing/acticityStop

{"activityid":500001403,"isStop":true}

'''
import requests
import json
import getCookie
def getActivityId(Cookie,pageIndex):
    #Cookie = getCookie.getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    url='https://www.shop2cn.com/service/mgmt/api/marketing/queryPromotionList?page=1&pageSize=30&activityStatus=1&activityType=3'
    data=requests.get(url=url,headers=headers,verify=False)
    #print(data.text)
    activityInfo=json.loads(data.text)['data']['records']
    return activityInfo

def deleteActivity(Cookie,id):
    #Cookie = getCookie.getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    url='https://www.shop2cn.com/service/mgmt/api/marketing/acticityStop'
    requestData={"activityid":id,"isStop":True}
    data=requests.post(url,headers=headers,json=requestData,verify=False)
    print(data.text)


if __name__ == '__main__':
    Cookie=getCookie.getCookies()
    infolist=getActivityId(Cookie,1)
    for item in infolist:
        deleteActivity(Cookie,item['activityId'])

