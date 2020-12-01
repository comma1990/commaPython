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