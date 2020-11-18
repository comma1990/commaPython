# author : comma
# date : 2020/11/18 10:06

'''
//div[@class="book-mid-info"]/h4/a/text()---------小说名
//div/p[@class="author"]/a[1]---------作者
https://www.qidian.com/rank/yuepiao
'''
import requests
import lxml.etree

url = 'https://www.qidian.com/rank/yuepiao'
headers = headers = {'Accept': 'application/json, text/plain, */*',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
resp = requests.get(url, headers=headers)
# print(resp.text)
e = lxml.etree.HTML(resp.text)
names = e.xpath('//div[@class="book-mid-info"]/h4/a/text()')
authors = e.xpath('//div/p[@class="author"]/a[1]/text()')

for name, author in zip(names, authors):
    print(name+':'+ author)
# print(names)
# print(authors)
