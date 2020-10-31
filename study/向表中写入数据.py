# author : comma
# date : 2020/10/14 12:44

# 将店铺的仓库id和名称保存到excel表中

import requests
import urllib3
import json
import openpyxl


def writeToExcel():
    wk = openpyxl.Workbook()
    sheet = wk.create_sheet()
    sheet.append(['仓库id', '仓库名', '买家展示名', '仓库图片'])

    from merchant_pc.getCookie import getCookies
    Cookie = getCookies()
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
    depotList = json.loads(response)['data']['depotList']
    for item in depotList:
        buyerName = item['buyerTitle']
        depotTitle = item['depotTitle']
        depotId = item['depotId']
        picUrl = item['picUrl']
        sheet.append([depotId, depotTitle, buyerName, picUrl])
        wk.save('D:\python\study\仓库信息.xlsx')  # 文件名重复的时候会报错，路径下文件删了重新执行就可以了


# depotId = json.loads(response)['data']['depotList'][1]['depotId']
#
# 定义成方法后，必须要在方法外部调用才会执行！！！
#
writeToExcel()
