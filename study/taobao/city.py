#author : comma
#date : 2021/3/17 10:18

import requests
import json
import urllib3

urllib3.disable_warnings()
url='https://h5api.m.taobao.com/h5/mtop.cainiao.geography.frontend.divisionsinfo.get/1.0/?jsv=2.5.1&appKey=12574478&t=1615947062395&sign=e2995c508ef070b3341e5bd77102e6f0&api=mtop.cainiao.geography.frontend.DivisionsInfo.get&v=1.0&dataType=jsonp&type=jsonp&callback=mtopjsonp5&data=%7B%22sn%22%3A%22suibianchuan%22%2C%22divisionToken%22%3A%22CN%22%2C%22pageIndex%22%3A1%2C%22pageSize%22%3A100%2C%22isFaultTolerant%22%3Atrue%7D HTTP/1.1'

headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               }
requestdata=requests.get(url,headers=headers,verify=False)
print(requestdata.text)
city=json.loads(requestdata.text)
print(city)