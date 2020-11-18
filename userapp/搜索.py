# author : comma
# date : 2020/11/18 15:33

'''
sit环境:sign:123
ymt-pars:
stg环境：'ymt-pars': 'format=json&accesstoken=1682F275632537FB2CF95D538EDE3CF9E85FF221546AD3C12D25A949E281A9C8CA23EE62AD0B229014314BD864D696633FF93E8225FFD49E&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=fd60bd09-1700-64da-84dc-a8770389cca5&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',

'''

import requests
import urllib.parse
import urllib3

urllib3.disable_warnings()

def search(keyword):

    url = 'https://api.shop2cn.com/sqbuyer/api/prod/sqsearch?AccessToken=1682F275632537FB2CF95D538EDE3CF9E85FF221546AD3C12D25A949E281A9C8CA23EE62AD0B229014314BD864D696633FF93E8225FFD49E&UserId=500002399&DeviceId=d2878bcdcfff42380be2babd027e6ed5'
    data = {"pageIndex": 1, "sortType": 1, "sortMode": 2, "keyword": "%E6%B5%B7%E8%93%9D%E4%B9%8B%E8%B0%9C"}
    headers = {'accept-version': '1.0.0', 'app-key': 'wxsqBuyer', 'app-version': '3.1.9',
               'ymt-pars': 'format=json&accesstoken=1682F275632537FB2CF95D538EDE3CF9E85FF221546AD3C12D25A949E281A9C8CA23EE62AD0B229014314BD864D696633FF93E8225FFD49E&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=fd60bd09-1700-64da-84dc-a8770389cca5&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',
               'sign': '123'
               }
    resp = requests.post(url, json=data, headers=headers, verify=False)
    print(resp.text)


if __name__ == '__main__':
    # w="%E6%B5%B7%E8%93%9D%E4%B9%8B%E8%B0%9C"
    # wp=urllib.parse.unquote(w)
    # print(wp)
    keyword={'key':'海蓝之谜'}
    zkey=urllib.parse.urlencode(keyword).split('=')[1]
    print(zkey)
    for i in range(2):
        search(zkey)
