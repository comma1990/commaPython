# author : comma
# date : 2020/10/28 15:09

# https://www.shop2cn.com/service/mgmt/api/marketing/sectionList?pageIndex=1&pageSize=20&sectionType=1
import requests
import json
import urllib3


def getSectionList(Cookie, sectionType):  # sectionType   1:限时抢，2：秒杀
    # from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    # Cookie = getCookies()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng, */*',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    urllib3.disable_warnings()
    data = requests.get(
        f'https://www.shop2cn.com/service/mgmt/api/marketing/sectionList?pageIndex=1&pageSize=20&sectionType={sectionType}',
        headers=headers,
        verify=False)
    response = data.text
    sectionList = json.loads(response)['data']['list']
    # print(sectionList)
    return sectionList


if __name__ == '__main__':
    from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie

    Cookie = getCookies()
    getSectionList(Cookie, 1)
