# author : comma
# date : 2020/11/18 15:33

'''
sit环境:sign:123

'ymt-pars': 'format=json&accesstoken=E0060D0BDE33BF408BF0715F97F8678EC699713F5017636808316D86FFDE3BD55518A89799268D655ECF21C2C04CF8075F057791AAE32ABE&userid=500967917&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=884df59b-a372-9a54-1c84-91ee98c1e4d8&idfa=187184a2a8e2d2804b5061470e2dce3d&imei=187184a2a8e2d2804b5061470e2dce3d&mchId=500041475',

stg环境：'ymt-pars': 'format=json&accesstoken=1682F275632537FB2CF95D538EDE3CF9E85FF221546AD3C12D25A949E281A9C8CA23EE62AD0B229014314BD864D696633FF93E8225FFD49E&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=fd60bd09-1700-64da-84dc-a8770389cca5&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',
https://api.shop2cn.com/sqbuyer/api/prod/sqsearch?AccessToken=1682F275632537FB1EC28A07F052B1EF88E2D6274C2090E03A1DBA1685CE0B54185D9C8B1328DB96E7B92B1D4CEF5BE029BB804BD7AE0A1C&UserId=500002399&DeviceId=d2878bcdcfff42380be2babd027e6ed5
'''

import requests
import urllib.parse
import urllib3

urllib3.disable_warnings()

def search(keyword):

    url = 'https://api.shop2cn.com/sqbuyer/api/prod/sqsearch?AccessToken=1682F275632537FBAEC3DFA86FD97BC2D8B2B4866B8F56940D2D59763EB5B241481FCF09822C0BB47517021D647F3C1731D270B3C2A806FF&UserId=500002399&DeviceId=d2878bcdcfff42380be2babd027e6ed5'
    data = {"pageIndex": 1, "sortType": 1, "sortMode": 0, "keyword": keyword}
    headers = {'accept-version': '1.0.0', 'app-key': 'wxsqBuyer', 'app-version': '3.1.9',
               'ymt-pars': 'format=json&accesstoken=1682F275632537FBAEC3DFA86FD97BC2D8B2B4866B8F56940D2D59763EB5B241481FCF09822C0BB47517021D647F3C1731D270B3C2A806FF&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=088fe54f-252d-18ba-fc3b-a10b268f90f2&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',
               'sign': '9df5193f8598b3f0b12af530ee530d86'
               }
    resp = requests.post(url, json=data, headers=headers, verify=False)
    print(resp.text)


if __name__ == '__main__':
    # w="%E6%B5%B7%E8%93%9D%E4%B9%8B%E8%B0%9C"
    # wp=urllib.parse.unquote(w)
    # print(wp)
    keyword={'key':'python商品31号'}
    zkey=urllib.parse.urlencode(keyword).split('=')[1]
    print(zkey)
    search(zkey)
    # for i in range(100):
    #     search(zkey)
