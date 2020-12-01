# author : comma
# date : 2020/11/30 15:09

'''
获取商品图片地址，并保存到mysql中
'''
import requests
import json
import mysql.connector
import urllib3


class getproductspic():
    def __init__(self):
        from merchant_pc.getCookie import getCookies
        Cookie = getCookies()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Cookie': Cookie}

    def send_request(self, i):
        pic_list = []
        urllib3.disable_warnings()
        url = 'https://www.shop2cn.com/service/order/api/product/list'
        data = {"pageIndex": i, "pageSize": 100, "agentType": -1, "deliveryTypes": [], "showType": 0, "status": "1"}
        resp = requests.post(url, headers=self.headers, json=data, verify=False)
        # print(resp.text)
        productlist = json.loads(resp.text)['data']['productList']
        for item in productlist:
            pic_list.append((item['pic'],))
        # print(pic_list)
        self.savepic(pic_list)

    def savepic(self, pic_list):
        conn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='haikun',
                                       auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        sql = 'insert into productpic (picUrl) values (%s)'
        cursor.executemany(sql, pic_list)
        conn.commit()
        print('共插入了', cursor.rowcount, '条数据')

    def start(self):
        for i in range(4,10):
            self.send_request(i)


if __name__ == '__main__':
    demo = getproductspic()
    demo.start()
    # demo.send_request(1)
