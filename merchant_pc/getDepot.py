# https://www.shop2cn.com/service/order/api/depot/getDepotList
# {"pageIndex":1,"pageSize":100}
import requests
import urllib3
import json


def getDepot(Cookie):
    # from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    requestData = {"pageIndex": 1, "pageSize": 100}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/depot/getDepotList', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    depotId = json.loads(response)['data']['depotList'][1]['depotId']
    # print('仓库编号：'+depotId)
    return depotId

if __name__ == '__main__':
    from merchant_pc import getCookie
    print(getDepot(getCookie.getCookies()))
