# author : comma
# date : 2020/11/18 18:38

'''
BeautifulSoup解析器:
    1.标准库   BeautifulSoup(html,'html.parse')    内置标准库，速度适中，文档容错能力强
    2.lxml HTML     BeautifulSoup(html,'lxml')    速度快，文档容错能力强
    3.lxml XML      BeautifulSoup(html,'xml')     速度快，唯一支持XML
    4.html5lib      BeautifulSoup(html,'html5lib)       容错能力最强，可生成HTML5

BeautifulSoup提取数据的常用方法
    find() : 提取满足要求的首个数据 使用方法：bs.find(标签，属性) 如：bs.find('div',class_='books') 返回值类型是tag
    find_all() : 提取满足要求的所有数据 使用方法：bs.find_all(标签，属性) 如：bs.find_all('div',class_='books') 返回值类型是tag
CSS选择器：
    通过ID查找：bs.select('#abc')
    通过class查找：bs.select('.abc')
    通过属性查找：bs.select(a['class="abc"'])
Tag对象：
    获取标签：bs.title
    获取所有属性：bs.title.attrs
    获取单个属性的值：bs.div.get('class')
                    bs.div['class']
                    bs.a['href']

'''

from bs4 import BeautifulSoup

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
bs = BeautifulSoup(html, 'lxml')
print(bs.title)  # 获取标签
print(bs.h1.attrs)  # 获取h1标签的所有属性

# 获取单个属性
print(bs.h1.get('class'))
print(bs.h1['class'])
print(bs.a['href'])

# 获取文本内容
print(bs.title.text)
print(bs.title.string)

# text和string的区别
print('----string获取的值-----', bs.h2.string)  # string可以获取所有的文本数据
print(bs.h2.text)  # text只能获取真正的值
print('---------分割线----------')

########## find提取数据 ##########
print(bs.find('div', class_='info'), type(bs.find('div', class_='info')))
print('-------下面是find_all 获取的数据-----------')
print(bs.find_all('div', class_='info'))  # 得到是一个标签的列表
print('---------下面遍历find_all获取的列表 -----------------')
for item in bs.find_all('div', class_='info'):
    print(item)
print('-------------------------------------------------------------')
print(bs.find_all('div',attrs={'float':'right'}))   # 根据属性的值来获取标签

########### select使用  ##############
print('---------------------CSS选择器----------------------------------------')
print(bs.select('#gb'))     # 根据ID获取值，值是一个列表


print('---------------------根据class获取值----------------------------------------')
print(bs.select('.info'))

print('---------------------根据路径获取----------------------------------------')
print(bs.select('div>span'))    # 获取div下面span的值

print('---------------------根据路径获取 2 ----------------------------------------')
print(bs.select('div.info>span'))
#获取值
for item in bs.select('div.info>span'):
    print(item.text)


