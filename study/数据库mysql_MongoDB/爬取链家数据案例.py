# author : comma
# date : 2020/11/25 17:09

import requests
from bs4 import BeautifulSoup
import mysql.connector
import urllib3


class LianJiaSpider():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='comma',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()

    def __init__(self):  # 初始化函数
        self.url = 'https://sh.lianjia.com/chengjiao/pg{0}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

    def send_request(self, url):  # 发送请求
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            return response

    def parse_html(self, resp):  # 解析html数据
        lst = []
        html = resp.text
        bs = BeautifulSoup(html, 'lxml')
        ul = bs.find('ul', class_='listContent')
        li_list = ul.find_all('li')
        for item in li_list:
            title = item.find('div', class_='title').text
            houseInfo = item.find('div', class_='houseInfo').text
            positionInfo = item.find('div', class_='positionInfo').text
            dealDate = item.find('div', class_='dealDate').text
            totalPrice = item.find('div', class_='totalPrice').text
            unitPrice = item.find('div', class_='unitPrice').text
            dealHouseTxt = item.find('span', class_='dealHouseTxt')
            if dealHouseTxt != None:
                dealHouseTxt = dealHouseTxt.text
            else:
                dealHouseTxt = ''

            span = item.find('span', class_='dealCycleTxt')
            span_list = span.find_all('span')

            agent_name = item.find('a', class_='agent_name').text
            lst.append((
                title, houseInfo, positionInfo, dealDate, totalPrice, unitPrice, dealHouseTxt, span_list[0].text,
                span_list[1].text, agent_name))
            # print(lst)
        self.save(lst)

    def save(self, lst):  # 保存数据
        sql = 'insert into db_lianjia(title, houseInfo, positionInfo, dealDate, totalPrice, unitPrice, dealHouseTxt, Listing_price, deal_cycle, agent_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.mycursor.executemany(sql, lst)
        self.mydb.commit()
        print('添加了', self.mycursor.rowcount, '条数据')

    def start(self):  # 启动
        urllib3.disable_warnings()
        for i in range(1, 5):
            full_url = self.url.format(i)
            resp = self.send_request(full_url)
            # print(resp.text)
            self.parse_html(resp)


if __name__ == '__main__':
    lianjia = LianJiaSpider()  # 初始化对象
    lianjia.start()
