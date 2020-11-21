# @Author  :  comma 
# @Date    :  2020-11-21 13:25


'''
JSON：
    JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，它是基于ECMAScript的一个子集
    JSON采用完全独立于语言的文本格式
    JSON在python中分别由list和dict组成

JSON模块的功能：
    json.dumps() : 实现python类型转化为json字符串，返回一个str对象，把一个python对象编码转换成json字符串
    json.loads() : 把json格式字符串解码转换成python对象，从json到python的类型转换
    json.dump() : 将python内置类型序列化为json对象后写入文件
    json.load() : 读取文件中json形式的字符串转化成python类型

'''
import json

# 把字符串转换成json类型(字典)
s='{"name":"逗号"}'
obj=json.loads(s)
print(obj)
print(type(obj))

# 把json对象（字典）转换成字符串类型
ss=json.dumps(obj,ensure_ascii=False)
print(ss)
print(type(ss))

# 把json对象(字典)保存到文件中
json.dump(obj,open('json.txt','w',encoding='utf-8'),ensure_ascii=False)

# 从文件中读取json数据(字典)
print('---------------从文件读取数据--------------------')
obj2=json.load(open('json.txt',encoding='utf-8'))
print(obj2)
print(type(obj2))