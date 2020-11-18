#author : comma
#date : 2020/11/18 18:38

'''
BeautifulSoup解析器:
    1.标准库   BeautifulSoup(html,'html.parse')    内置标准库，速度适中，文档容错能力强
    2.lxml HTML     BeautifulSoup(html,'lxml')    速度快，文档容错能力强
    3.lxml XML      BeautifulSoup(html,'xml')     速度快，唯一支持XML
    4.html5lib      BeautifulSoup(html,'html5lib)       容错能力最强，可生成HTML5

'''

import bs4.builder._lxml

html='''
        <html>
            <head>
                <title>comma学习记录</title>
            </head>
        </html>


'''