# author : comma
# date : 2020/11/26 18:27
'''
交易流程验证
?AccessToken=1682F275632537FBDE1FFA1F5AB8127DA6DA530F2BE5CBF37F0073CB23504CE18491F962500E84FC37B928C9204FCDD2D7D23685C883967F&UserId=500002399&DeviceId=d2878bcdcfff42380be2babd027e6ed5
'''
import requests
import urllib3
import json


class TransactionProcess():
    def __init__(self):
        self.headers = {
            'ymt-pars': 'format=json&accesstoken=1682F275632537FBDE1FFA1F5AB8127DA6DA530F2BE5CBF37F0073CB23504CE18491F962500E84FC37B928C9204FCDD2D7D23685C883967F&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=01ce1260-397e-4128-0f6f-78dedc5471cc&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',
            'app-key': 'wxsqBuyer',
            'cookieid': 'd2878bcdcfff42380be2babd027e6ed5',
            'accept-version': '1.0.0',
            'sign': '9df5193f8598b3f0b12af530ee530d86'}

    def searchallproducts(self):  # 判断全部商品是否为空，不为空返回第一个商品id
        url = 'https://api.shop2cn.com/sqbuyer/api/prod/sqsearch'
        data = {"pageIndex": 1, "sortType": 1, "sortMode": 0, "keyword": ""}
        resp = requests.post(url, headers=self.headers, json=data, verify=False)
        # print(resp.text)
        product = json.loads(resp.text)
        if len(product['list']) != 0:
            # print(product['list'][0]['id'])
            return product['list'][0]['id']

        else:
            print('------------------全部商品无数据，请检查')

    def productdetail(self, productId): # 获取商品详情
        url = 'https://api.shop2cn.com/sqbuyer/api/prod/sqdetail?productid={0}'.format(productId)
        resp = requests.get(url, headers=self.headers, verify=False)
        json_data = json.loads(resp.text)
        print(resp.text)


if __name__ == '__main__':
    urllib3.disable_warnings()
    tp = TransactionProcess()
    productId = tp.searchallproducts()  # 判断全部商品是否为空，不为空返回第一个商品id
    tp.productdetail(productId)
