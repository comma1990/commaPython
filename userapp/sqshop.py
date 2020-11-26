# author : comma
# date : 2020/11/26 16:37

'''
AccessToken=1682F275632537FBDE1FFA1F5AB8127DA6DA530F2BE5CBF37F0073CB23504CE18491F962500E84FC37B928C9204FCDD2D7D23685C883967F&
?UserId=500002399&DeviceId=d2878bcdcfff42380be2babd027e6ed5&MerchantId=500002398
'''
import json

import requests
import urllib3


class UserInterface():
    def __init__(self):
        self.headers = {
            'ymt-pars': 'format=json&accesstoken=1682F275632537FBDE1FFA1F5AB8127DA6DA530F2BE5CBF37F0073CB23504CE18491F962500E84FC37B928C9204FCDD2D7D23685C883967F&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=01ce1260-397e-4128-0f6f-78dedc5471cc&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',
            'app-key': 'wxsqBuyer',
            'cookieid': 'd2878bcdcfff42380be2babd027e6ed5',
            'accept-version': '1.0.0',
            'sign': '9df5193f8598b3f0b12af530ee530d86'}

    def sqshop(self):  # 这个接口版本号需要是2.0.0，所以单独设置headers
        headers = {
            'ymt-pars': 'format=json&accesstoken=1682F275632537FBDE1FFA1F5AB8127DA6DA530F2BE5CBF37F0073CB23504CE18491F962500E84FC37B928C9204FCDD2D7D23685C883967F&userid=500002399&network=wifi&client=ios&os=iOS%2013.3.1&machineName=iPhone%20X%20(GSM%2BCDMA)%3CiPhone10%2C3%3E&requestid=01ce1260-397e-4128-0f6f-78dedc5471cc&idfa=d2878bcdcfff42380be2babd027e6ed5&imei=d2878bcdcfff42380be2babd027e6ed5&mchId=500002398',
            'app-key': 'wxsqBuyer',
            'cookieid': 'd2878bcdcfff42380be2babd027e6ed5',
            'accept-version': '2.0.0',
            'sign': '9df5193f8598b3f0b12af530ee530d86'}
        url = 'https://api.shop2cn.com/sqbuyer/api/prod/sqshop?MerchantId=500002398'
        resp = requests.get(url, headers=headers, verify=False)
        json_data = json.loads(resp.text)
        # print(resp.text)
        return json_data

    def shophomepartdata(self, partid):
        url = 'https://api.shop2cn.com/sqbuyer/api/prod/shophomepartdata?PartId={0}'.format(partid)
        resp = requests.get(url, headers=self.headers, verify=False)
        json_data = json.loads(resp.text)
        # print(resp.text)
        return json_data


if __name__ == '__main__':
    urllib3.disable_warnings()
    user = UserInterface()
    result = user.sqshop()
    name = result['name']
    if name == '蜡笔小新':
        print('接口调用成功')
    else:
        print('接口调用失败')

    parts = result['parts']
    for item in parts:
        if item['skinCode'] == 'shop-header':  # 首页页头
            print(item['name'])
        if item['skinCode'] == 'product-spec':  # 获取专题模块partId
            # print(item['partId'])
            departmentdata = user.shophomepartdata(item['partId'])
            if len(departmentdata['list'][0]['productList']) != 0:  # 判断专题页是否有数据
                print(departmentdata['list'][0]['name'], '有商品数据返回')
            else:
                print('-------------------------无商品数据返回，请手动验证,专题名称：', departmentdata['list'][0]['name'])
            if departmentdata['list'][0]['picList'][0]['picUrl'] != None:  # 判断专题页是否有头图返回
                print(departmentdata['list'][0]['name'], '有图片数据返回')
            else:
                print('-------------------------无商品数据返回，请手动验证,专题名称：', departmentdata['list'][0]['name'])
