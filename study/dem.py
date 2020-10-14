# author : comma
# date : 2020/10/14 12:28
import requests
import urllib3
import json
import time

#date=time.DATE()
#s='${DATE}'
print(help(time))




# def getDepot():
#     from merchant_pc.getCookie import getCookies
#     Cookie = getCookies()
#     headers = {'Accept': 'application/json, text/plain, */*',
#                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
#                'Host': 'www.shop2cn.com',
#                'Connection': 'keep - alive',
#                'Cookie': Cookie
#                }
#     #x = random.randint(10, 50)
#     #loginId = 'kfzg' + str(x)
#     #title = '客服主管' + str(x)
#     '''设置角色id——templateId'''
#     requestData = {"pageIndex":1,"pageSize":100}
#     urllib3.disable_warnings()
#     data = requests.post('https://www.shop2cn.com/service/order/api/product/list', json=requestData,
#                          headers=headers,
#                          verify=False)
#     response = data.text
#     print(response)
