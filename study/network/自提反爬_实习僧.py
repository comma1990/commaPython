#author : comma
#date : 2020/12/12 12:36

'''
爬取数字的时候发现是乱码，F12定位元素的值，复制出来后通过utf-8编码，三个字节为一个字符，找出规律

print('-/天'.encode('utf-8'))
b'\xee\x83\xb4\xee\x93\xa6\xee\xb1\x99-\xee\x83\xb4\xee\x81\x91\xee\xb1\x99/\xe5\xa4\xa9'--->'120-180/天'

\xee\x83\xb4--->1
\xee\x93\xa6--->2
\xee\xb1\x99--->0
\xee\x81\x91--->8
'''

import requests
import urllib3
from bs4 import BeautifulSoup


urllib3.disable_warnings()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
def send_request():
    url='https://www.shixiseng.com/interns?keyword=python&page=1&city=%E5%85%A8%E5%9B%BD&type=intern'
    response=requests.get(url,headers=headers,verify=False)
    # print(response.text)
    return response.text

def detail_url(url):
    html=requests.get(url,headers=headers,verify=False)
    #解析职位详情页面
    bs=BeautifulSoup(html.text,'html.parser')
    title=bs.title.text # 招聘职位名称
    # 获取公司名称
    company_name=bs.select('.com_intro .com-name')[0].text # 首先获取class=’com_intro‘ 的标签，然后获取它的下级class=com-name的标签，中间用空格隔开
    # 获取薪水
    salary=bs.select('.job_money.cutom_font')[0].text.encode('utf-8') # 获取class="job_money cutom_font"的标签，因为class是两个属性修饰的，中间不加空格
    # salary=salary.replace('\xe5\xa4\xa9','天')
    salary=salary.replace(b'\xee\x83\xb4',b'1')
    salary=salary.replace(b'\xee\x93\xa6',b'2')
    salary=salary.replace(b'\xee\xb1\x99',b'0')
    salary=salary.replace(b'\xee\x81\x91',b'8')
    salary=salary.replace(b'\xee\xa2\xa9',b'3')
    salary=salary.replace(b'\xef\x82\x81',b'5')
    salary=salary.decode('utf-8')
    print(title,company_name,salary)



def parse_html(html):
    bs=BeautifulSoup(html,'html.parser')
    offers=bs.select('.intern-wrap.intern-item')
    # print(offers[0])
    for offer in offers:
        url=offer.select('.f-l.intern-detail__job a')[0]['href']
        # print(url)
        # print('\n')
        detail_url(url)


if __name__ == '__main__':
    html=send_request()
    parse_html(html)
