# author : comma
# date : 2020/11/18 10:06

'''
使用xpath选取节点
nodename : 选取此节点的所有子节点
/   : 从根节点选择
//  : 从匹配选择的当前节点选择文档中的节点，而不考虑他们的位置
.   : 选取当前节点
..  : 选取当前节点的父节点
/text() : 获取当前路径下的文本内容
/@xxx   : 提取当前路径下标签的属性值
|可选符  : 可选取若干个路径//p|//div,在当前路径下选取所有符合条件的p标签和div标签

表达式：
xpath('/body/div[1]')   : 选取body下的第一个div节点
xpath('/body/div[last()]')    : 选取body下最后一个div节点
xpath('/baody/div[last()-1]')   :选取body下倒数第二个div节点
xpath('/body/div[postition()<3]')   : 选取body下前两个div节点
xpath('/body/div[@class]')  : 选取body下带有class属性的div节点
xpath('/body/div[@calss="main"]')   : 选取body下class属性为main的div节点
xpath('/body/div[price>35.00]') : 选取body下price元素大于35的div节点

'''
# //div[@class="book-mid-info"]/h4/a/text() ----获取小说名称
# //p[@class="author"]/a[1]/text() -------获取作者名字
import requests
import lxml.etree

url = 'https://www.qidian.com/rank/yuepiao'
headers = {'Accept': 'application/json, text/plain, */*',
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
