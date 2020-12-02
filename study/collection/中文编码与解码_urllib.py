# author : comma
# date : 2020/12/1 17:48

import urllib.parse

keyword = {'key': '海蓝之谜'}

# 编码
x = urllib.parse.urlencode(keyword)

# 截取值部分
y=x.split('=')[1]   #字符串分割split
print(x)
print(y)

# 解码
m=urllib.parse.unquote(y)
print(m)


#### 根据输入的值解码
jie=urllib.parse.unquote('prods%5B0%5D=c43698914%2C1%2C50%2C101')
print(jie)