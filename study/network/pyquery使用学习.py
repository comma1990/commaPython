# @Author  :  comma 
# @Date    :  2020-11-21 11:00

'''
pyquery的解析数据
    1.获取当前节点    doc('#main')
    2.获取子节点     doc('#main').children()
    3.获取父节点     doc('#main').parent()
    4.获取兄弟节点    doc('#main').siblings()
    5.获取属性      doc('#main').attr('href')
    5.获取内容      doc('#main').html()     doc('#main').text()

'''
import pyquery

html = '''
        <html>
            <head>
                <title>comma学习记录</title>
            </head>
            <div class="info" float="left">
                逗号小菜鸡
            </div>
            <div class="info" float="right" id="gb">
                <span>小菜鸡要努力学习</span>
                <a href="www.comma.com">官网</a>
            </div>
            <span>一个外部的span，和上面的区别开</span>
            <body>
                <h1 class="info bg" float='left'>comma好好学习，天天向上</H1>
                <a href="https://www.baidu.com">百度</a>
                <h2><!------注释--------></h2>
            </body>
        </html>
'''
############ 字符串方式初始化 #################
from pyquery import PyQuery as pq

doc = pq(html)  # 创建PyQuery的对象，实际上就是在进行一个类型转换，将str类型转换成PyQuery类型
print(doc)
print(type(doc))
print(doc('title'))  # 获取title标签内容

############ 通过url初始化 ####################
print('-------------------------- 通过url初始化PyQuery -------------------------------------')
from pyquery import PyQuery as py1

doc1 = py1(url='https://www.baidu.com', encoding='utf-8')
print(doc1)
print(doc1('title'))

############ 文件初始化PyQuery ####################
print('-------------------------- 通过文件初始化PyQuery -------------------------------------')
from pyquery import PyQuery as pq2

doc2 = pq2(filename='百度.html')
print(doc2('title'))
print(doc2('link').attr('href'))

############# 获取节点及属性 #############
print('-------------------------- 获取当前节点 -------------------------------------')
print(doc2('#head'))
print('-------------------------- 获取父节点 -------------------------------------')
print(doc2('#head').parent())
print('-------------------------- 获取子节点 -------------------------------------')
print(doc2('#head').children())
print('-------------------------- 获取兄弟节点（同级） -------------------------------------')
print(doc2('#head').siblings())
print('-------------------------- 获取内容html()_所有内容都打印出来 -------------------------------------')
print(doc2('#head').html())
print('-------------------------- 获取内容text()_只获取文本内容 -------------------------------------')
print(doc2('#head').text())

############# 案例：爬取起点小说月票排行榜的书名，作者 #########################
print('-------------------------- 案例-------------------------------------')

import requests
import urllib3
from pyquery import PyQuery as pq3
urllib3.disable_warnings()
url3 = 'https://www.qidian.com/rank/yuepiao'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
responsedata=requests.get(url3,headers=headers)
# print(responsedata.text)
doca=pq3(responsedata.text)
# print(doca)
# a_tag=doca('h4 a')
names=[a.text for a in doca('h4 a')]
print(names)

authors=doca('p.author a')
author_lst=[]
for index in range(len(authors)):
    if index%2==0:
        author_lst.append(authors[index].text)
print(author_lst)

for name,author in zip(names,author_lst):
    print(name+':'+author)